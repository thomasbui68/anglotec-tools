"""
AngloTec Study Bot - Configuration
=====================================
All settings and configuration for the Telegram bot.
"""

import os
from datetime import time

# ============================================================
# BOT TOKEN
# ============================================================
# Get your bot token from @BotFather on Telegram
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# ============================================================
# BOT INFO
# ============================================================
BOT_NAME = "AngloTec Study Bot"
BOT_USERNAME = "anglotec_study_bot"  # Change after creating with @BotFather
BOT_VERSION = "1.0.0"

# ============================================================
# ANGLOTEC BRANDING
# ============================================================
# These URLs are promoted subtly in every interaction
ANGLOTEC_URLS = {
    "tools": "https://tools.anglotec-ai.com",
    "ielts_calculator": "https://tools.anglotec-ai.com/ielts-calculator",
    "oet_practice": "https://tools.anglotec-ai.com/oet-practice",
    "osce_generator": "https://tools.anglotec-ai.com/osce-generator",
    "nhs_interview": "https://tools.anglotec-ai.com/nhs-interview-bank",
    "study_planner": "https://tools.anglotec-ai.com/study-planner",
    "vocab_app": "https://tools.anglotec-ai.com/vocabulary",
    "main": "https://anglotec-ai.com",
}

# Footer appended to most messages (subtle promotion)
ANGLOTEC_FOOTER = (
    "\n\n━━━━━━━━━━━━━━━━━━━━\n"
    "📚 <b>More Free Tools</b>\n"
    "🌐 tools.anglotec-ai.com\n"
    "✨ IELTS Calculator • OET Practice • OSCE Generator"
)

# Short footer for shorter messages
ANGLOTEC_FOOTER_SHORT = "\n\n🌐 More at tools.anglotec-ai.com"

# ============================================================
# ADMIN SETTINGS
# ============================================================
# Admin user IDs for management commands (optional)
ADMIN_IDS = [
    # Add admin Telegram user IDs here, e.g., 123456789
]

# ============================================================
# SCHEDULER SETTINGS
# ============================================================
# Time for daily auto-posts (UTC)
DAILY_POST_TIME = time(hour=9, minute=0)  # 9:00 AM UTC

# Days of the week for themed posts
# 0=Monday, 6=Sunday
THEME_SCHEDULE = {
    0: "ielts_vocab",      # Monday: IELTS vocabulary
    1: "oet_speaking",     # Tuesday: OET speaking tip
    2: "osce_station",     # Wednesday: OSCE station type
    3: "ai_prompt",        # Thursday: AI prompt of the day
    4: "nhs_value",        # Friday: NHS value of the week
    5: "motivation",       # Saturday: Study motivation
    6: "weekly_challenge", # Sunday: Weekly challenge
}

# ============================================================
# FEATURE FLAGS
# ============================================================
ENABLE_QUIZ = True
ENABLE_STUDY_PLAN = True
ENABLE_CALCULATOR = True
ENABLE_AUTO_POSTS = True
ENABLE_SUBSCRIPTION = True

# ============================================================
# STUDY PLAN SETTINGS
# ============================================================
MIN_STUDY_WEEKS = 1
MAX_STUDY_WEEKS = 52
DEFAULT_STUDY_WEEKS = 8

# IELTS band score thresholds
IELTS_BAND_THRESHOLDS = {
    9.0: (39, 40),   # Academic Reading out of 40
    8.5: (37, 38),
    8.0: (35, 36),
    7.5: (33, 34),
    7.0: (30, 32),
    6.5: (27, 29),
    6.0: (23, 26),
    5.5: (19, 22),
    5.0: (15, 18),
    4.5: (13, 14),
    4.0: (10, 12),
    3.5: (8, 9),
    3.0: (6, 7),
    2.5: (4, 5),
}

# ============================================================
# DATABASE
# ============================================================
# Simple JSON file storage for subscribers
SUBSCRIBERS_FILE = "subscribers.json"
QUIZ_STATS_FILE = "quiz_stats.json"

# ============================================================
# LOGGING
# ============================================================
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
