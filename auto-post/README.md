# AngloTec AI Auto-Post Script

Automated social media posting for Reddit, Twitter (X), and LinkedIn. Promotes AngloTec AI tools at `https://tools.anglotec-ai.com`.

## Features

### Reddit Module (`--reddit`)
- Posts to 8 targeted subreddits: `r/IELTS`, `r/nursing`, `r/medicalschool`, `r/ChatGPT`, `r/languagelearning`, `r/studyAbroad`, `r/PLAB`, `r/NHS`
- 20+ pre-written post templates across 5 categories
- Duplicate prevention via JSON history tracking
- Auto-reply to comments (`--reply-comments`)
- Staggered posting with random delays (3-10 min between posts)
- Optimal time targeting (UK/US overlap hours)

### Twitter Module (`--twitter`)
- Single tweets with hashtags
- Thread posting (3-5 connected tweets)
- Image tweets (with media upload support)
- 8 hashtag sets for strategic rotation
- Daily frequency limit (default: 3x/day)

### LinkedIn Module (`--linkedin`)
- Professional article-style posts
- Tool link sharing with commentary
- Group posting support (requires group IDs)
- Weekly frequency limit (default: 2x/week)

### Shared Features
- **Environment variable configuration** for all API keys
- **JSON posting history** to prevent duplicates
- **Dry-run mode** (`--dry-run`) to preview posts
- **Configurable posting frequency** via config.json
- **Comprehensive logging** with timestamps and URLs
- **Error handling and retry logic** with jitter delays
- **Clean, modular architecture** with separate classes per platform

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file or export directly:

```bash
# Reddit API Credentials
export REDDIT_CLIENT_ID="your_reddit_client_id"
export REDDIT_SECRET="your_reddit_secret"
export REDDIT_USERNAME="your_reddit_username"
export REDDIT_PASSWORD="your_reddit_password"
export REDDIT_USER_AGENT="AngloTecBot/1.0 by /u/your_username"

# Twitter API Credentials (v2 + v1.1 for media)
export TWITTER_API_KEY="your_twitter_api_key"
export TWITTER_API_SECRET="your_twitter_api_secret"
export TWITTER_ACCESS_TOKEN="your_access_token"
export TWITTER_ACCESS_SECRET="your_access_secret"
export TWITTER_BEARER_TOKEN="your_bearer_token"

# LinkedIn API Credentials
export LINKEDIN_ACCESS_TOKEN="your_linkedin_access_token"
export LINKEDIN_PERSON_URN="your_person_urn"  # Optional; auto-fetched if not set
```

### 3. Preview (Dry Run)

```bash
python autopost.py --dry-run
```

This shows exactly what WOULD be posted without making any actual API calls.

### 4. Run for Real

```bash
# Post to all platforms on schedule
python autopost.py --schedule

# Or post to specific platforms
python autopost.py --reddit
python autopost.py --twitter
python autopost.py --linkedin

# Reply to Reddit comments
python autopost.py --reply-comments
```

---

## Project Structure

```
auto-post/
├── autopost.py           # Main script
├── config.json           # Post templates and configuration
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── logs/                 # Log files (auto-created)
│   └── autopost_YYYYMMDD.log
├── posted_history.json   # Post tracking (auto-created)
├── images/               # Image assets for Twitter
└── .last_*_post          # Frequency markers (auto-created)
```

---

## API Key Setup Guide

### Reddit API Keys
1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" (select "script")
3. Copy Client ID and Secret
4. Use your Reddit username and password

### Twitter API Keys
1. Go to https://developer.twitter.com/en/portal/dashboard
2. Create a new project and app
3. Generate API Key, Secret, Access Token, and Access Secret
4. Enable Read + Write permissions
5. Generate Bearer Token

### LinkedIn API Token
1. Go to https://www.linkedin.com/developers/
2. Create an app
3. Request access to "Share on LinkedIn" and "Sign In with LinkedIn v2"
4. Generate a 3-legged OAuth access token
5. Alternatively, use 2-legged OAuth for personal accounts

---

## Post Template Categories

### IELTS/UKVI (5 Templates)
- Writing checker promotion
- Free mock test alternative
- Task 2 structure guide
- Speaking practice
- Band score improvement stories

### OET/Nursing (5 Templates)
- OET writing checker for nurses
- NMC registration pathway
- Referral letter writing guide
- IELTS vs OET comparison
- NHS new recruit resources

### OSCE/PLAB/Medical (5 Templates)
- PLAB 2 OSCE practice
- Passed PLAB experience sharing
- Communication stations guide
- Common mistakes breakdown
- Free OSCE station simulator

### AI/Prompt Engineering (5 Templates)
- Medical exam-specific prompts
- Prompt engineering guide
- ChatGPT fine-tuning results
- Before/after prompt comparison
- Open-source project sharing

### General Brand Awareness (5 Templates)
- Free tools collection overview
- Open-source project announcement
- 30-day experiment results
- Study abroad pathway guide
- Community feedback request

---

## Configuration

### config.json

| Key | Description | Default |
|-----|-------------|---------|
| `tool_url` | URL promoted in all posts | `https://tools.anglotec-ai.com` |
| `frequency.reddit_per_day` | Max Reddit posts per day | 3 |
| `frequency.twitter_per_day` | Max tweets per day | 3 |
| `frequency.linkedin_per_week` | Max LinkedIn posts per week | 2 |
| `linkedin_group_ids` | LinkedIn group IDs for group posting | `[]` |

### Template Structure

Each template includes:
- `id` - Unique identifier for deduplication
- `category` - Content category
- `title` - Post title (Reddit/LinkedIn)
- `body` - Post body text
- `cta` - Call-to-action with `{tool_url}` placeholder
- `subreddit` - Target subreddit (Reddit only)
- `hashtags` - Hashtag sets (Twitter only)
- `best_time_utc` - Optimal posting hour (UTC)
- `tags` - Internal categorization

---

## Scheduling

### Optimal Posting Times (UTC)

| Platform | Optimal Hours | Rationale |
|----------|--------------|-----------|
| Reddit | 09:00, 12:00, 15:00, 18:00 | UK morning, US morning overlap |
| Twitter | 08:00, 13:00, 17:00 | Morning commute, lunch, evening |
| LinkedIn | 09:00, 14:00 | UK business hours |

### Recommended Cron Setup

```bash
# Reddit: Daily at 9 AM UTC
0 9 * * * cd /path/to/auto-post && python autopost.py --reddit

# Twitter: 3x daily at 8 AM, 1 PM, 5 PM UTC
0 8,13,17 * * * cd /path/to/auto-post && python autopost.py --twitter

# LinkedIn: Tuesdays and Thursdays at 2 PM UTC
0 14 * * 2,4 cd /path/to/auto-post && python autopost.py --linkedin

# Reddit comment replies: Daily at 6 PM UTC
0 18 * * * cd /path/to/auto-post && python autopost.py --reply-comments
```

---

## Logging

All activity is logged to `logs/autopost_YYYYMMDD.log`:

```
2024-01-15 09:00:01 | INFO     | RedditModule  | Posted to r/IELTS: https://reddit.com/r/IELTS/comments/...
2024-01-15 09:05:23 | INFO     | TwitterModule | Tweeted: https://twitter.com/i/web/status/...
2024-01-15 09:10:45 | ERROR    | LinkedInModule| LinkedIn post failed: 401 - Unauthorized
```

---

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--dry-run` | Preview what would be posted (no actual posts) |
| `--reddit` | Post to Reddit only |
| `--twitter` | Post to Twitter only |
| `--linkedin` | Post to LinkedIn only |
| `--reply-comments` | Reply to Reddit comments on recent posts |
| `--schedule` | Run full scheduled posting (default behavior) |
| `--config PATH` | Use custom config file |

---

## Requirements

- Python 3.8+
- `praw` (Reddit API)
- `tweepy` (Twitter API)
- `requests` (LinkedIn API)
- API keys for Reddit, Twitter, and LinkedIn

---

## License

MIT License - Free for personal and commercial use.

---

## Support

For issues or questions, check the log files in the `logs/` directory for detailed error messages.
