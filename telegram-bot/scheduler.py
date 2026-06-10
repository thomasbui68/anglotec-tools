"""
AngloTec Study Bot - Daily Auto-Post Scheduler
=================================================
Handles daily themed posts for subscribers.
Uses python-telegram-bot's built-in JobQueue for scheduling.
"""

import logging
import json
import os
from datetime import datetime, time
from typing import Optional

from telegram.ext import Application, ContextTypes
from telegram.constants import ParseMode

from config import (
    DAILY_POST_TIME,
    THEME_SCHEDULE,
    SUBSCRIBERS_FILE,
    ENABLE_AUTO_POSTS,
)
from responses import (
    get_monday_vocab,
    get_tuesday_oet_tip,
    get_wednesday_osce_tip,
    get_thursday_ai_prompt,
    get_friday_nhs_value,
    get_saturday_motivation,
    get_sunday_challenge,
    get_daily_vocab,
)

logger = logging.getLogger(__name__)


# ============================================================
# SUBSCRIBER MANAGEMENT
# ============================================================

def load_subscribers() -> set[int]:
    """Load subscriber chat IDs from file."""
    if not os.path.exists(SUBSCRIBERS_FILE):
        return set()
    try:
        with open(SUBSCRIBERS_FILE, "r") as f:
            data = json.load(f)
            return set(data.get("subscribers", []))
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Error loading subscribers: {e}")
        return set()


def save_subscribers(subscribers: set[int]) -> None:
    """Save subscriber chat IDs to file."""
    try:
        with open(SUBSCRIBERS_FILE, "w") as f:
            json.dump({"subscribers": sorted(list(subscribers))}, f, indent=2)
    except IOError as e:
        logger.error(f"Error saving subscribers: {e}")


def add_subscriber(chat_id: int) -> bool:
    """Add a subscriber. Returns True if newly added, False if already subscribed."""
    subscribers = load_subscribers()
    if chat_id in subscribers:
        return False
    subscribers.add(chat_id)
    save_subscribers(subscribers)
    logger.info(f"New subscriber added: {chat_id}. Total: {len(subscribers)}")
    return True


def remove_subscriber(chat_id: int) -> bool:
    """Remove a subscriber. Returns True if removed, False if not found."""
    subscribers = load_subscribers()
    if chat_id not in subscribers:
        return False
    subscribers.remove(chat_id)
    save_subscribers(subscribers)
    logger.info(f"Subscriber removed: {chat_id}. Total: {len(subscribers)}")
    return True


def is_subscriber(chat_id: int) -> bool:
    """Check if a chat is subscribed."""
    return chat_id in load_subscribers()


def get_subscriber_count() -> int:
    """Get total number of subscribers."""
    return len(load_subscribers())


# ============================================================
# CONTENT GENERATORS BY DAY
# ============================================================

CONTENT_GENERATORS = {
    "ielts_vocab": get_monday_vocab,
    "oet_speaking": get_tuesday_oet_tip,
    "osce_station": get_wednesday_osce_tip,
    "ai_prompt": get_thursday_ai_prompt,
    "nhs_value": get_friday_nhs_value,
    "motivation": get_saturday_motivation,
    "weekly_challenge": get_sunday_challenge,
}


def get_content_for_today() -> Optional[str]:
    """Get the themed content for today."""
    weekday = datetime.now().weekday()  # 0=Monday
    theme_key = THEME_SCHEDULE.get(weekday)
    
    if theme_key and theme_key in CONTENT_GENERATORS:
        generator = CONTENT_GENERATORS[theme_key]
        try:
            return generator()
        except Exception as e:
            logger.error(f"Error generating content for {theme_key}: {e}")
            # Fallback to vocabulary
            return get_daily_vocab(count=2)
    
    return None


def get_day_name(weekday: int) -> str:
    """Get day name from weekday number."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday]


# ============================================================
# SCHEDULER FUNCTIONS
# ============================================================

def setup_scheduler(application: Application) -> None:
    """Set up the daily auto-post scheduler."""
    if not ENABLE_AUTO_POSTS:
        logger.info("Auto-posts are disabled in config.")
        return
    
    # Schedule daily post at configured time (UTC)
    application.job_queue.run_daily(
        daily_post_callback,
        time=DAILY_POST_TIME,
        name="daily_study_post",
    )
    
    logger.info(
        f"Daily scheduler set up for {DAILY_POST_TIME.hour:02d}:{DAILY_POST_TIME.minute:02d} UTC. "
        f"({len(load_subscribers())} subscribers)"
    )


async def daily_post_callback(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback function for daily posts."""
    subscribers = load_subscribers()
    
    if not subscribers:
        logger.info("No subscribers to send daily post to.")
        return
    
    content = get_content_for_today()
    if not content:
        logger.warning("No content generated for today.")
        return
    
    weekday = datetime.now().weekday()
    day_name = get_day_name(weekday)
    theme_key = THEME_SCHEDULE.get(weekday, "unknown")
    
    logger.info(f"Sending daily post to {len(subscribers)} subscribers. Theme: {theme_key} ({day_name})")
    
    sent_count = 0
    failed_count = 0
    
    for chat_id in subscribers:
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=content,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=False,
            )
            sent_count += 1
        except Exception as e:
            logger.error(f"Failed to send daily post to {chat_id}: {e}")
            failed_count += 1
            # If the bot was blocked, remove the subscriber
            if "blocked" in str(e).lower() or "deactivated" in str(e).lower():
                remove_subscriber(chat_id)
                logger.info(f"Removed blocked subscriber: {chat_id}")
    
    logger.info(f"Daily post complete: {sent_count} sent, {failed_count} failed.")


async def send_test_post(context: ContextTypes.DEFAULT_TYPE, chat_id: int) -> None:
    """Send a test post to a specific chat (for admin testing)."""
    content = get_content_for_today()
    if content:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"🧪 <b>TEST POST</b>\n\n{content}",
            parse_mode=ParseMode.HTML,
        )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ No content available for today.",
            parse_mode=ParseMode.HTML,
        )


async def broadcast_message(context: ContextTypes.DEFAULT_TYPE, message: str, sender_id: int) -> None:
    """Broadcast a message to all subscribers (admin only)."""
    subscribers = load_subscribers()
    
    sent = 0
    failed = 0
    
    for chat_id in subscribers:
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=message,
                parse_mode=ParseMode.HTML,
            )
            sent += 1
        except Exception as e:
            logger.error(f"Broadcast failed to {chat_id}: {e}")
            failed += 1
    
    # Confirm to sender
    await context.bot.send_message(
        chat_id=sender_id,
        text=f"📢 Broadcast complete: {sent} sent, {failed} failed.",
        parse_mode=ParseMode.HTML,
    )
