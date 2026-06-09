#!/usr/bin/env python3
"""
AngloTec AI Auto-Posting Script
================================
Automated social media posting for Reddit, Twitter, and LinkedIn.
Promotes AngloTec AI tools at https://tools.anglotec-ai.com

Usage:
    python autopost.py --dry-run          # Preview what would be posted
    python autopost.py --reddit           # Post only to Reddit
    python autopost.py --twitter          # Post only to Twitter
    python autopost.py --linkedin         # Post only to LinkedIn
    python autopost.py --schedule         # Run on schedule (default)
    python autopost.py --reply-comments   # Reply to comments on Reddit
"""

import os
import sys
import json
import time
import random
import logging
import argparse
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict

# Third-party imports
import requests

# ---------------------------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------------------------
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"autopost_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)-12s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("AngloTecAutoPost")


# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------
@dataclass
class PostRecord:
    """Tracks a posted item to prevent duplicates."""

    platform: str
    template_id: str
    target: str  # subreddit, hashtag set, or LinkedIn group
    post_url: str
    posted_at: str
    title: str = ""
    content_hash: str = ""
    engagement: Dict = None

    def __post_init__(self):
        if self.engagement is None:
            self.engagement = {}


# ---------------------------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------------------------
def load_config(config_path: str = "config.json") -> Dict:
    """Load configuration and templates from JSON file."""
    path = Path(config_path)
    if not path.is_absolute():
        path = Path(__file__).parent / path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_posted_history(history_file: str = "posted_history.json") -> List[Dict]:
    """Load history of previously posted content."""
    path = Path(__file__).parent / history_file
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_posted_history(history: List[Dict], history_file: str = "posted_history.json"):
    """Save posting history to JSON file."""
    path = Path(__file__).parent / history_file
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    logger.info(f"History saved to {path} ({len(history)} records)")


def hash_content(content: str) -> str:
    """Generate a content hash for deduplication."""
    return hashlib.sha256(content.encode()).hexdigest()[:16]


def jitter_delay(base_seconds: float, jitter_percent: float = 0.2):
    """Sleep with random jitter to avoid predictable patterns."""
    jitter = base_seconds * jitter_percent * (2 * random.random() - 1)
    time.sleep(max(0, base_seconds + jitter))


def format_template(template: Dict, tool_url: str = "https://tools.anglotec-ai.com") -> Dict:
    """Replace {tool_url} placeholder in template fields."""
    result = {}
    for key, value in template.items():
        if isinstance(value, str):
            result[key] = value.replace("{tool_url}", tool_url)
        elif isinstance(value, list):
            result[key] = [
                v.replace("{tool_url}", tool_url) if isinstance(v, str) else v
                for v in value
            ]
        elif isinstance(value, dict):
            result[key] = {
                k: (v.replace("{tool_url}", tool_url) if isinstance(v, str) else v)
                for k, v in value.items()
            }
        else:
            result[key] = value
    return result


# ---------------------------------------------------------------------------
# Reddit Module
# ---------------------------------------------------------------------------
class RedditModule:
    """Handles posting to Reddit via PRAW."""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.logger = logging.getLogger("RedditModule")
        self.subreddits = [
            "IELTS",
            "nursing",
            "medicalschool",
            "ChatGPT",
            "languagelearning",
            "studyAbroad",
            "PLAB",
            "NHS",
        ]
        self.posted = load_posted_history()
        self._init_client()

    def _init_client(self):
        """Initialize the Reddit PRAW client."""
        try:
            import praw
            client_id = os.environ.get("REDDIT_CLIENT_ID", "")
            client_secret = os.environ.get("REDDIT_SECRET", "")
            username = os.environ.get("REDDIT_USERNAME", "")
            password = os.environ.get("REDDIT_PASSWORD", "")
            user_agent = os.environ.get(
                "REDDIT_USER_AGENT",
                "AngloTecAIBot/1.0 by /u/" + (username or "unknown"),
            )

            if not all([client_id, client_secret, username, password]):
                self.logger.warning(
                    "Reddit credentials not fully configured. Set REDDIT_CLIENT_ID, "
                    "REDDIT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD env vars."
                )
                self.reddit = None
                return

            self.reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password,
                user_agent=user_agent,
            )
            self.logger.info(f"Reddit client initialized as {username}")
        except ImportError:
            self.logger.error("praw library not installed. Run: pip install praw")
            self.reddit = None
        except Exception as e:
            self.logger.error(f"Reddit init error: {e}")
            self.reddit = None

    def _already_posted(self, template_id: str, subreddit: str) -> bool:
        """Check if this template was already posted to this subreddit."""
        for record in self.posted:
            if (
                record.get("platform") == "reddit"
                and record.get("template_id") == template_id
                and record.get("target") == subreddit
            ):
                return True
        return False

    def _pick_templates(self, templates: List[Dict], count: int = 3) -> List[Dict]:
        """Select templates that haven't been posted to their target subreddits."""
        candidates = []
        for tpl in templates:
            if not self._already_posted(tpl["id"], tpl.get("subreddit", "")):
                candidates.append(tpl)
        if len(candidates) < count:
            self.logger.warning(
                f"Only {len(candidates)} unposted templates available"
            )
        random.shuffle(candidates)
        return candidates[:count]

    def post(self, templates: List[Dict]):
        """Post content to Reddit subreddits."""
        if not self.reddit and not self.dry_run:
            self.logger.error("Reddit client not available. Skipping.")
            return

        selected = self._pick_templates(templates)
        self.logger.info(f"Selected {len(selected)} templates for Reddit")

        for tpl in selected:
            tpl = format_template(tpl)
            subreddit = tpl.get("subreddit", "")
            title = tpl.get("title", "")
            body = tpl.get("body", "")
            best_time = tpl.get("best_time_utc", "09:00")

            if self.dry_run:
                self.logger.info(
                    f"[DRY-RUN] Would post to r/{subreddit}: {title[:80]}..."
                )
                continue

            if not subreddit or not title:
                self.logger.warning(f"Skipping template {tpl.get('id')} - missing fields")
                continue

            # Stagger posts
            delay = random.randint(180, 600)  # 3-10 minutes
            self.logger.info(f"Waiting {delay}s before posting to r/{subreddit}...")
            jitter_delay(delay)

            try:
                sub = self.reddit.subreddit(subreddit)
                post = sub.submit(title=title, selftext=body)
                post_url = f"https://reddit.com{post.permalink}"

                record = PostRecord(
                    platform="reddit",
                    template_id=tpl["id"],
                    target=subreddit,
                    post_url=post_url,
                    posted_at=datetime.utcnow().isoformat() + "Z",
                    title=title[:200],
                    content_hash=hash_content(title + body),
                )
                self.posted.append(asdict(record))
                save_posted_history(self.posted)
                self.logger.info(f"Posted to r/{subreddit}: {post_url}")

            except Exception as e:
                self.logger.error(f"Failed posting to r/{subreddit}: {e}")
                continue

    def reply_to_comments(self, max_replies: int = 5):
        """Auto-reply to comments on recent posts."""
        if not self.reddit and not self.dry_run:
            self.logger.error("Reddit client not available. Skipping.")
            return

        reply_templates = [
            "Thanks for your interest! You can check out the tool here: {tool_url}",
            "Glad you found it helpful! More features at {tool_url}",
            "Feel free to try it out and share feedback: {tool_url}",
            "Absolutely! Here's the link if you want to explore: {tool_url}",
            "Happy to help! Check out {tool_url} for more tools.",
        ]

        reddit_username = os.environ.get("REDDIT_USERNAME", "")
        reply_count = 0

        for record in self.posted:
            if record.get("platform") != "reddit" or reply_count >= max_replies:
                break

            post_url = record.get("post_url", "")
            if not post_url:
                continue

            try:
                # Extract post ID from URL
                parts = post_url.split("/")
                if len(parts) < 5:
                    continue
                post_id = parts[4] if "comments" in parts else None
                if not post_id:
                    continue

                submission = self.reddit.submission(id=post_id)
                submission.comments.replace_more(limit=0)

                for comment in submission.comments[:3]:  # Check top 3 comments
                    if comment.author and comment.author.name != reddit_username:
                        # Check if already replied
                        already_replied = any(
                            reply.author
                            and reply.author.name == reddit_username
                            for reply in comment.replies
                        )
                        if not already_replied:
                            reply_text = random.choice(reply_templates).replace(
                                "{tool_url}", "https://tools.anglotec-ai.com"
                            )

                            if self.dry_run:
                                self.logger.info(
                                    f"[DRY-RUN] Would reply to comment on {post_url}"
                                )
                                reply_count += 1
                                continue

                            comment.reply(reply_text)
                            self.logger.info(f"Replied to comment on {post_url}")
                            reply_count += 1
                            jitter_delay(30)

                            if reply_count >= max_replies:
                                break

            except Exception as e:
                self.logger.error(f"Error replying to comments on {post_url}: {e}")
                continue

        self.logger.info(f"Processed {reply_count} comment replies")


# ---------------------------------------------------------------------------
# Twitter Module
# ---------------------------------------------------------------------------
class TwitterModule:
    """Handles posting tweets and threads via Tweepy."""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.logger = logging.getLogger("TwitterModule")
        self.hashtag_sets = [
            "#IELTS #LanguageLearning #StudyAbroad",
            "#OET #Nursing #NHS #Healthcare",
            "#OSCE #PLAB2 #Medical #PLAB",
            "#AI #PromptEngineering #ChatGPT",
            "#IELTS #AI #EdTech #LanguageLearning",
            "#NHS #Nursing #OET #UKJobs",
            "#PLAB2 #OSCE #MedicalSchool #StudyTips",
            "#PromptEngineering #AI #TechTips",
        ]
        self.posted = load_posted_history()
        self._init_client()

    def _init_client(self):
        """Initialize the Twitter/Tweepy client."""
        try:
            import tweepy

            api_key = os.environ.get("TWITTER_API_KEY", "")
            api_secret = os.environ.get("TWITTER_API_SECRET", "")
            access_token = os.environ.get("TWITTER_ACCESS_TOKEN", "")
            access_secret = os.environ.get("TWITTER_ACCESS_SECRET", "")
            bearer_token = os.environ.get("TWITTER_BEARER_TOKEN", "")

            if not all([api_key, api_secret, access_token, access_secret]):
                self.logger.warning(
                    "Twitter credentials not fully configured. Set TWITTER_API_KEY, "
                    "TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET env vars."
                )
                self.client = None
                return

            # v2 Client for tweeting
            self.client = tweepy.Client(
                bearer_token=bearer_token or None,
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_secret,
            )

            # v1.1 API for media uploads (images)
            auth = tweepy.OAuthHandler(api_key, api_secret)
            auth.set_access_token(access_token, access_secret)
            self.api = tweepy.API(auth, wait_on_rate_limit=True)

            self.logger.info("Twitter client initialized")
        except ImportError:
            self.logger.error("tweepy library not installed. Run: pip install tweepy")
            self.client = None
        except Exception as e:
            self.logger.error(f"Twitter init error: {e}")
            self.client = None

    def _already_posted(self, template_id: str) -> bool:
        """Check if this template was already posted today."""
        today = datetime.utcnow().strftime("%Y-%m-%d")
        for record in self.posted:
            if (
                record.get("platform") == "twitter"
                and record.get("template_id") == template_id
                and record.get("posted_at", "").startswith(today)
            ):
                return True
        return False

    def post_tweet(self, templates: List[Dict]):
        """Post a single tweet."""
        if not self.client and not self.dry_run:
            self.logger.error("Twitter client not available. Skipping.")
            return

        available = [t for t in templates if not self._already_posted(t["id"])]
        if not available:
            self.logger.info("No new tweet templates available for today")
            return

        tpl = format_template(random.choice(available))
        hashtags = random.choice(self.hashtag_sets)
        text = f"{tpl.get('body', '')}\n\n{hashtags}\n\n{t.get('cta', '')}".replace("{tool_url}", "https://tools.anglotec-ai.com")

        # Truncate if needed
        if len(text) > 280:
            text = text[:277] + "..."

        if self.dry_run:
            self.logger.info(f"[DRY-RUN] Would tweet:\n{text[:100]}...")
            return

        try:
            response = self.client.create_tweet(text=text)
            tweet_id = response.data["id"]
            tweet_url = f"https://twitter.com/i/web/status/{tweet_id}"

            record = PostRecord(
                platform="twitter",
                template_id=tpl["id"],
                target="timeline",
                post_url=tweet_url,
                posted_at=datetime.utcnow().isoformat() + "Z",
                content_hash=hash_content(text),
            )
            self.posted.append(asdict(record))
            save_posted_history(self.posted)
            self.logger.info(f"Tweeted: {tweet_url}")

        except Exception as e:
            self.logger.error(f"Failed to tweet: {e}")

    def post_thread(self, thread_templates: List[Dict]):
        """Post a thread of connected tweets (3-5 tweets)."""
        if not self.client and not self.dry_run:
            self.logger.error("Twitter client not available. Skipping.")
            return

        # Pick a thread template set
        available = [t for t in thread_templates if not self._already_posted(t["id"])]
        if not available:
            self.logger.info("No new thread templates available")
            return

        tpl = format_template(random.choice(available))
        tweets = tpl.get("thread", [])
        if not tweets or len(tweets) < 2:
            self.logger.warning("Thread has too few tweets, skipping")
            return

        cta = tpl.get("cta", "").replace("{tool_url}", "https://tools.anglotec-ai.com")
        hashtags = random.choice(self.hashtag_sets)

        if self.dry_run:
            self.logger.info(f"[DRY-RUN] Would post thread of {len(tweets)} tweets")
            for i, t in enumerate(tweets[:5]):
                self.logger.info(f"  Tweet {i+1}: {t[:80]}...")
            return

        previous_tweet_id = None
        posted_urls = []

        for i, tweet_text in enumerate(tweets[:5]):  # Max 5 tweets
            text = tweet_text.replace("{tool_url}", "https://tools.anglotec-ai.com")
            if i == len(tweets) - 1 and cta:
                text += f"\n\n{cta}\n{hashtags}"
            if len(text) > 280:
                text = text[:277] + "..."

            try:
                if previous_tweet_id:
                    response = self.client.create_tweet(
                        text=text, in_reply_to_tweet_id=previous_tweet_id
                    )
                else:
                    response = self.client.create_tweet(text=text)

                tweet_id = response.data["id"]
                previous_tweet_id = tweet_id
                tweet_url = f"https://twitter.com/i/web/status/{tweet_id}"
                posted_urls.append(tweet_url)

                jitter_delay(15)  # Brief pause between tweets

            except Exception as e:
                self.logger.error(f"Thread tweet {i+1} failed: {e}")
                break

        if posted_urls:
            record = PostRecord(
                platform="twitter",
                template_id=tpl["id"],
                target="thread",
                post_url=posted_urls[0],
                posted_at=datetime.utcnow().isoformat() + "Z",
                content_hash=hash_content(json.dumps(tweets)),
            )
            self.posted.append(asdict(record))
            save_posted_history(self.posted)
            self.logger.info(f"Posted thread with {len(posted_urls)} tweets")

    def post_with_image(self, image_templates: List[Dict], image_dir: str = "images"):
        """Post a tweet with an attached image."""
        if not self.client and not self.dry_run:
            self.logger.error("Twitter client not available. Skipping.")
            return

        available = [t for t in image_templates if not self._already_posted(t["id"])]
        if not available:
            self.logger.info("No new image tweet templates available")
            return

        tpl = format_template(random.choice(available))
        text = tpl.get("body", "").replace("{tool_url}", "https://tools.anglotec-ai.com")
        hashtags = random.choice(self.hashtag_sets)
        full_text = f"{text}\n\n{hashtags}"
        if len(full_text) > 280:
            full_text = full_text[:277] + "..."

        image_path = tpl.get("image_path", "")
        if image_path and not Path(image_path).is_absolute():
            image_path = str(Path(__file__).parent / image_dir / image_path)

        if self.dry_run:
            self.logger.info(f"[DRY-RUN] Would tweet with image:\n{full_text[:80]}...")
            return

        try:
            media_id = None
            if image_path and Path(image_path).exists():
                media = self.api.media_upload(image_path)
                media_id = media.media_id

            if media_id:
                response = self.client.create_tweet(text=full_text, media_ids=[media_id])
            else:
                response = self.client.create_tweet(text=full_text)

            tweet_id = response.data["id"]
            tweet_url = f"https://twitter.com/i/web/status/{tweet_id}"

            record = PostRecord(
                platform="twitter",
                template_id=tpl["id"],
                target="timeline_image",
                post_url=tweet_url,
                posted_at=datetime.utcnow().isoformat() + "Z",
                content_hash=hash_content(full_text),
            )
            self.posted.append(asdict(record))
            save_posted_history(self.posted)
            self.logger.info(f"Tweeted with image: {tweet_url}")

        except Exception as e:
            self.logger.error(f"Failed to tweet with image: {e}")


# ---------------------------------------------------------------------------
# LinkedIn Module
# ---------------------------------------------------------------------------
class LinkedInModule:
    """Handles posting to LinkedIn via REST API."""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.logger = logging.getLogger("LinkedInModule")
        self.access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "")
        self.person_urn = os.environ.get("LINKEDIN_PERSON_URN", "")
        self.posted = load_posted_history()
        self.base_url = "https://api.linkedin.com/v2"

        if not self.access_token:
            self.logger.warning(
                "LinkedIn access token not configured. Set LINKEDIN_ACCESS_TOKEN env var."
            )

    def _headers(self) -> Dict:
        """Build request headers with auth."""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        }

    def _get_person_urn(self) -> Optional[str]:
        """Fetch the authenticated user's person URN."""
        if self.person_urn:
            return self.person_urn
        try:
            url = f"{self.base_url}/userinfo"
            resp = requests.get(url, headers=self._headers(), timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                sub = data.get("sub", "")
                if sub:
                    self.person_urn = f"urn:li:person:{sub}"
                    return self.person_urn
        except Exception as e:
            self.logger.error(f"Failed to get person URN: {e}")
        return None

    def _already_posted_this_week(self, template_id: str) -> bool:
        """Check if this template was posted within the last 7 days."""
        week_ago = datetime.utcnow() - timedelta(days=7)
        for record in self.posted:
            if (
                record.get("platform") == "linkedin"
                and record.get("template_id") == template_id
            ):
                posted_at = record.get("posted_at", "")
                try:
                    posted_dt = datetime.fromisoformat(posted_at.replace("Z", "+00:00").replace("+00:00", ""))
                    if posted_dt > week_ago:
                        return True
                except Exception:
                    continue
        return False

    def post_article(self, templates: List[Dict]):
        """Post a professional article-style update to LinkedIn."""
        if not self.access_token and not self.dry_run:
            self.logger.error("LinkedIn access token not available. Skipping.")
            return

        urn = self._get_person_urn()
        if not urn and not self.dry_run:
            self.logger.error("Could not determine LinkedIn person URN")
            return

        available = [
            t for t in templates if not self._already_posted_this_week(t["id"])
        ]
        if not available:
            self.logger.info("No new LinkedIn templates available this week")
            return

        tpl = format_template(random.choice(available))
        title = tpl.get("title", "")
        body = tpl.get("body", "").replace("\n", "\n\n")
        cta = tpl.get("cta", "").replace("{tool_url}", "https://tools.anglotec-ai.com")

        share_commentary = f"{title}\n\n{body}"
        if cta:
            share_commentary += f"\n\n{cta}"

        payload = {
            "author": urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": share_commentary},
                    "shareMediaCategory": "ARTICLE",
                    "media": [
                        {
                            "status": "READY",
                            "originalUrl": "https://tools.anglotec-ai.com",
                            "title": {"text": title or "AngloTec AI Tools"},
                        }
                    ],
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }

        if self.dry_run:
            self.logger.info(f"[DRY-RUN] Would post to LinkedIn:\n{share_commentary[:120]}...")
            return

        try:
            url = f"{self.base_url}/ugcPosts"
            resp = requests.post(url, headers=self._headers(), json=payload, timeout=30)
            if resp.status_code in (200, 201):
                post_urn = resp.headers.get("x-restli-id", "")
                post_url = f"https://www.linkedin.com/feed/update/{post_urn}"

                record = PostRecord(
                    platform="linkedin",
                    template_id=tpl["id"],
                    target="personal_feed",
                    post_url=post_url,
                    posted_at=datetime.utcnow().isoformat() + "Z",
                    content_hash=hash_content(share_commentary),
                )
                self.posted.append(asdict(record))
                save_posted_history(self.posted)
                self.logger.info(f"Posted to LinkedIn: {post_url}")
            else:
                self.logger.error(f"LinkedIn post failed: {resp.status_code} - {resp.text[:200]}")

        except Exception as e:
            self.logger.error(f"LinkedIn post error: {e}")

    def post_tool_link(self, templates: List[Dict]):
        """Post a tool link with professional commentary."""
        if not self.access_token and not self.dry_run:
            self.logger.error("LinkedIn access token not available. Skipping.")
            return

        urn = self._get_person_urn()
        if not urn and not self.dry_run:
            return

        available = [
            t for t in templates if not self._already_posted_this_week(t["id"])
        ]
        if not available:
            self.logger.info("No new LinkedIn link templates available this week")
            return

        tpl = format_template(random.choice(available))
        body = tpl.get("body", "")
        cta = tpl.get("cta", "").replace("{tool_url}", "https://tools.anglotec-ai.com")

        full_text = f"{body}\n\n{cta}" if cta else body

        payload = {
            "author": urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": full_text},
                    "shareMediaCategory": "ARTICLE",
                    "media": [
                        {
                            "status": "READY",
                            "originalUrl": "https://tools.anglotec-ai.com",
                            "title": {"text": tpl.get("title", "AngloTec AI")},
                            "description": {
                                "text": tpl.get("description", "AI-powered tools for professionals")
                            },
                        }
                    ],
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }

        if self.dry_run:
            self.logger.info(f"[DRY-RUN] Would share link on LinkedIn:\n{full_text[:120]}...")
            return

        try:
            url = f"{self.base_url}/ugcPosts"
            resp = requests.post(url, headers=self._headers(), json=payload, timeout=30)
            if resp.status_code in (200, 201):
                post_urn = resp.headers.get("x-restli-id", "")
                post_url = f"https://www.linkedin.com/feed/update/{post_urn}"

                record = PostRecord(
                    platform="linkedin",
                    template_id=tpl["id"],
                    target="personal_feed",
                    post_url=post_url,
                    posted_at=datetime.utcnow().isoformat() + "Z",
                    content_hash=hash_content(full_text),
                )
                self.posted.append(asdict(record))
                save_posted_history(self.posted)
                self.logger.info(f"Shared tool link on LinkedIn: {post_url}")
            else:
                self.logger.error(
                    f"LinkedIn link share failed: {resp.status_code} - {resp.text[:200]}"
                )

        except Exception as e:
            self.logger.error(f"LinkedIn link share error: {e}")

    def post_to_groups(self, group_templates: List[Dict], group_ids: List[str] = None):
        """Post to LinkedIn groups (requires group IDs)."""
        if not self.access_token and not self.dry_run:
            self.logger.error("LinkedIn access token not available. Skipping.")
            return

        if not group_ids:
            self.logger.info("No LinkedIn group IDs configured. Skipping group posts.")
            return

        urn = self._get_person_urn()
        if not urn and not self.dry_run:
            return

        for tpl in group_templates[:2]:  # Max 2 group posts per run
            tpl = format_template(tpl)
            body = tpl.get("body", "")

            for group_id in group_ids[:1]:  # One group per template
                payload = {
                    "author": urn,
                    "lifecycleState": "PUBLISHED",
                    "specificContent": {
                        "com.linkedin.ugc.ShareContent": {
                            "shareCommentary": {"text": body},
                            "shareMediaCategory": "NONE",
                        }
                    },
                    "visibility": {
                        "com.linkedin.ugc.MemberNetworkVisibility": "CONTAINER"
                    },
                    "containerEntity": f"urn:li:group:{group_id}",
                }

                if self.dry_run:
                    self.logger.info(
                        f"[DRY-RUN] Would post to LinkedIn group {group_id}:\n{body[:80]}..."
                    )
                    continue

                try:
                    url = f"{self.base_url}/ugcPosts"
                    resp = requests.post(url, headers=self._headers(), json=payload, timeout=30)
                    if resp.status_code in (200, 201):
                        self.logger.info(f"Posted to LinkedIn group {group_id}")
                    else:
                        self.logger.error(
                            f"Group post failed: {resp.status_code} - {resp.text[:200]}"
                        )
                    jitter_delay(30)

                except Exception as e:
                    self.logger.error(f"LinkedIn group post error: {e}")


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------
class PostScheduler:
    """Manages posting frequency and timing across platforms."""

    def __init__(self, config: Dict):
        self.config = config
        self.logger = logging.getLogger("Scheduler")

    def should_post_reddit(self) -> bool:
        """Check if Reddit should post today (once daily)."""
        last_post_file = Path(__file__).parent / ".last_reddit_post"
        if not last_post_file.exists():
            return True
        last_date = last_post_file.read_text().strip()
        today = datetime.utcnow().strftime("%Y-%m-%d")
        if last_date == today:
            self.logger.info("Reddit already posted today. Skipping.")
            return False
        return True

    def should_post_twitter(self) -> bool:
        """Check if Twitter should post (up to 3x/day)."""
        history = load_posted_history()
        today = datetime.utcnow().strftime("%Y-%m-%d")
        today_posts = [
            r
            for r in history
            if r.get("platform") == "twitter" and r.get("posted_at", "").startswith(today)
        ]
        max_tweets = self.config.get("frequency", {}).get("twitter_per_day", 3)
        if len(today_posts) >= max_tweets:
            self.logger.info(f"Twitter already posted {len(today_posts)} times today. Skipping.")
            return False
        return True

    def should_post_linkedin(self) -> bool:
        """Check if LinkedIn should post (2x/week)."""
        history = load_posted_history()
        now = datetime.utcnow()
        week_ago = now - timedelta(days=7)
        week_posts = [
            r
            for r in history
            if r.get("platform") == "linkedin"
            and datetime.fromisoformat(
                r.get("posted_at", "1970-01-01").replace("Z", "+00:00").replace("+00:00", "")
            )
            > week_ago
        ]
        max_posts = self.config.get("frequency", {}).get("linkedin_per_week", 2)
        if len(week_posts) >= max_posts:
            self.logger.info(
                f"LinkedIn already posted {len(week_posts)} times this week. Skipping."
            )
            return False
        return True

    def mark_posted(self, platform: str):
        """Mark a platform as posted for today."""
        marker = Path(__file__).parent / f".last_{platform}_post"
        marker.write_text(datetime.utcnow().strftime("%Y-%m-%d"))

    def optimal_time_offset(self, platform: str) -> int:
        """Return optimal posting hour offset (UTC) for platform."""
        optimal_times = {
            "reddit": [9, 12, 15, 18],  # UTC hours for UK/US overlap
            "twitter": [8, 13, 17],  # Morning, noon, evening
            "linkedin": [9, 14],  # Business hours
        }
        hours = optimal_times.get(platform, [12])
        target_hour = random.choice(hours)
        now = datetime.utcnow()
        target = now.replace(hour=target_hour, minute=random.randint(0, 59))
        if target < now:
            target += timedelta(days=1)
        delay = int((target - now).total_seconds())
        return max(0, delay)


# ---------------------------------------------------------------------------
# Main Orchestrator
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="AngloTec AI Auto-Posting Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python autopost.py --dry-run                # Preview all posts
  python autopost.py --reddit                 # Post to Reddit only
  python autopost.py --twitter                # Tweet only
  python autopost.py --linkedin               # LinkedIn only
  python autopost.py --reply-comments         # Reply to Reddit comments
  python autopost.py --schedule               # Run on full schedule (default)
        """,
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    parser.add_argument("--reddit", action="store_true", help="Post to Reddit only")
    parser.add_argument("--twitter", action="store_true", help="Post to Twitter only")
    parser.add_argument("--linkedin", action="store_true", help="Post to LinkedIn only")
    parser.add_argument("--reply-comments", action="store_true", help="Reply to Reddit comments")
    parser.add_argument("--schedule", action="store_true", help="Run on schedule (default)")
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to config file (default: config.json)",
    )
    args = parser.parse_args()

    dry_run = args.dry_run

    if dry_run:
        logger.info("=" * 60)
        logger.info("DRY RUN MODE - No actual posts will be made")
        logger.info("=" * 60)

    # Load configuration
    config = load_config(args.config)
    templates = config.get("templates", {})
    frequency = config.get("frequency", {})

    # Initialize modules
    reddit = RedditModule(dry_run=dry_run)
    twitter = TwitterModule(dry_run=dry_run)
    linkedin = LinkedInModule(dry_run=dry_run)
    scheduler = PostScheduler(config)

    # Determine what to run
    run_reddit = args.reddit or args.schedule or not (args.twitter or args.linkedin or args.reply_comments)
    run_twitter = args.twitter or args.schedule or not (args.reddit or args.linkedin or args.reply_comments)
    run_linkedin = args.linkedin or args.schedule or not (args.reddit or args.twitter or args.reply_comments)
    run_replies = args.reply_comments

    logger.info("=" * 60)
    logger.info("AngloTec AI Auto-Post Starting")
    logger.info(f"Time (UTC): {datetime.utcnow().isoformat()}")
    logger.info(f"Platforms: Reddit={run_reddit}, Twitter={run_twitter}, LinkedIn={run_linkedin}")
    logger.info(f"Reply mode: {run_replies}")
    logger.info("=" * 60)

    # ---- Reddit ----
    if run_reddit and (dry_run or scheduler.should_post_reddit()):
        reddit_templates = templates.get("reddit", [])
        if reddit_templates:
            reddit.post(reddit_templates)
            if not dry_run:
                scheduler.mark_posted("reddit")
        else:
            logger.warning("No Reddit templates found in config")

    # ---- Twitter ----
    if run_twitter and (dry_run or scheduler.should_post_twitter()):
        tweet_templates = templates.get("twitter", [])
        thread_templates = templates.get("twitter_threads", [])
        image_templates = templates.get("twitter_images", [])

        if tweet_templates:
            twitter.post_tweet(tweet_templates)
        if thread_templates:
            twitter.post_thread(thread_templates)
        if image_templates:
            twitter.post_with_image(image_templates)

    # ---- LinkedIn ----
    if run_linkedin and (dry_run or scheduler.should_post_linkedin()):
        linkedin_templates = templates.get("linkedin", [])
        linkedin_link_templates = templates.get("linkedin_links", [])
        linkedin_group_templates = templates.get("linkedin_groups", [])
        group_ids = config.get("linkedin_group_ids", [])

        if linkedin_templates:
            linkedin.post_article(linkedin_templates)
        if linkedin_link_templates:
            linkedin.post_tool_link(linkedin_link_templates)
        if linkedin_group_templates and group_ids:
            linkedin.post_to_groups(linkedin_group_templates, group_ids)

    # ---- Comment Replies ----
    if run_replies:
        reddit.reply_to_comments(max_replies=5)

    logger.info("=" * 60)
    logger.info("AngloTec AI Auto-Post Complete")
    logger.info(f"Log file: {LOG_FILE}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
