"""
AngloTec Study Bot - Configuration
====================================
All settings and configuration for the Discord bot.
"""

import os

# ── Discord Bot Token ──────────────────────────────────────────────────────────
# Get your bot token from: https://discord.com/developers/applications
# Create a New Application > Bot > Copy Token
# Set it as an environment variable: export DISCORD_BOT_TOKEN=your_token_here
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# ── Bot Identity ─────────────────────────────────────────────────────────────
BOT_NAME = "AngloTec Study Bot"
BOT_DESCRIPTION = (
    "A helpful study companion for IELTS, OET, OSCE, PLAB, and NHS preparation. "
    "I provide genuine tips, resources, and free tools to help you succeed."
)
BOT_PREFIX = "!"
BOT_ACTIVITY = "Studying with you | !help"

# ── Channel & Server Settings ────────────────────────────────────────────────
# Leave empty to respond in all channels the bot can see
# Or add specific channel IDs as integers: [123456789, 987654321]
ALLOWED_CHANNEL_IDS = []  # Empty = all channels

# Server IDs where the bot is active (for analytics or restrictions)
# Empty = all servers
ALLOWED_GUILD_IDS = []

# ── Rate Limiting (Anti-Spam) ────────────────────────────────────────────────
# Only respond to 1 in every N messages (higher = less frequent responses)
RESPONSE_CHANCE = 5  # 1 in 5 messages

# Delay before responding (seconds) - random range for natural feel
MIN_RESPONSE_DELAY = 30   # minimum seconds to wait
MAX_RESPONSE_DELAY = 120  # maximum seconds to wait

# Maximum responses per channel per hour (prevents spam)
MAX_RESPONSES_PER_CHANNEL_PER_HOUR = 3

# Cooldown between responses in the same channel (seconds)
CHANNEL_COOLDOWN_SECONDS = 600  # 10 minutes

# ── Keyword Monitoring ───────────────────────────────────────────────────────
# Keywords that trigger the bot to respond
MONITORED_KEYWORDS = [
    # IELTS related
    "ielts", "band score", "band 7", "band 8", "band 6", "band 5",
    "listening test", "reading test", "writing test", "speaking test",
    "ielts speaking", "ielts writing", "ielts reading", "ielts listening",
    "academic ielts", "general ielts", "ielts preparation",

    # OET related
    "oet", "occupational english test", "oet nursing", "oet medicine",
    "oet writing", "oet speaking", "oet reading", "oet listening",
    "oet roleplay", "oet letter", "referral letter",

    # OSCE / PLAB related
    "osce", "plab", "plab 1", "plab 2", "clinical exam",
    "objective structured clinical examination",
    "nmc registration", "nmc test of competence",

    # NHS related
    "nhs", "nhs interview", "nhs job", "band 5", "band 6",
    "healthcare assistant", "hca", "nhs trust",

    # Study / Career related
    "study uk", "work in uk", "nursing uk", "nurse uk",
    "overseas nurse", "international nurse", "foreign nurse",
    "cbt exam", "computer based test",

    # Emotion / Struggle keywords
    "worried", "nervous", "stressed", "struggling", "failed",
    "help me", "any tips", "any advice", "dont know how",
]

# ── AngloTec Tool Links ──────────────────────────────────────────────────────
# These are the free tools the bot subtly links to
TOOL_LINKS = {
    "ielts_calculator": "https://anglotec.co.uk/ielts-band-score-calculator",
    "ielts_speaking": "https://anglotec.co.uk/ielts-speaking-practice",
    "ielts_writing": "https://anglotec.co.uk/ielts-writing-checklist",
    "ielts_reading": "https://anglotec.co.uk/ielts-reading-tips",
    "oet_writing": "https://anglotec.co.uk/oet-writing-checklist",
    "oet_speaking": "https://anglotec.co.uk/oet-roleplay-generator",
    "oet_reading": "https://anglotec.co.uk/oet-reading-tips",
    "osce_generator": "https://anglotec.co.uk/osce-scenario-generator",
    "nhs_interview": "https://anglotec.co.uk/nhs-interview-bank",
    "nhs_cv": "https://anglotec.co.uk/nhs-cv-builder",
    "plab_tips": "https://anglotec.co.uk/plab-preparation",
    "study_planner": "https://anglotec.co.uk/study-planner",
}

# ── Bot Personality ──────────────────────────────────────────────────────────
# Tone and style settings
BOT_PERSONALITY = {
    "tone": "friendly, encouraging, and knowledgeable",
    "style": "conversational, like a supportive study partner",
    "never_say": [
        "click here",
        "sign up now",
        "limited time",
        "act fast",
        "don't miss out",
        "exclusive offer",
        "buy now",
        "discount",
        "promo",
        "deal",
    ],
    "preferred_phrases": [
        "We built a free tool that might help...",
        "I found this useful when I was preparing...",
        "There's a free calculator at...",
        "You might find this helpful...",
        "A lot of people use this free tool...",
    ],
}

# ── Logging ──────────────────────────────────────────────────────────────────
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "bot.log"

# ── Admin Settings ───────────────────────────────────────────────────────────
# Discord user IDs of bot admins (can use admin commands)
ADMIN_USER_IDS = []
