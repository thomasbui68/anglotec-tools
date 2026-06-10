"""
AngloTec Study Bot - Main Telegram Bot
========================================
A powerful Telegram bot for IELTS, OET & OSCE study preparation.
Works in both private chats and groups. Provides daily study content,
quizzes, vocabulary, and study plans while promoting AngloTec tools.

Usage:
    python bot.py

Requirements:
    - Python 3.9+
    - python-telegram-bot[job-queue]
    - Set BOT_TOKEN environment variable
"""

import logging
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
from telegram.constants import ParseMode

from config import (
    BOT_TOKEN,
    BOT_NAME,
    BOT_VERSION,
    ENABLE_QUIZ,
    ENABLE_STUDY_PLAN,
    ENABLE_CALCULATOR,
    ENABLE_SUBSCRIPTION,
    ADMIN_IDS,
    LOG_LEVEL,
    LOG_FORMAT,
    ANGLOTEC_URLS,
    ANGLOTEC_FOOTER_SHORT,
)
from responses import (
    get_welcome_message,
    get_help_message,
    get_ielts_resources,
    get_oet_resources,
    get_osce_resources,
    get_nhs_resources,
    get_daily_vocab,
    get_study_tips,
    generate_study_plan,
    calculate_ielts_band,
)
from quiz import (
    get_random_question,
    format_question,
    format_answer,
    get_quiz_stats,
)
from scheduler import (
    setup_scheduler,
    add_subscriber,
    remove_subscriber,
    is_subscriber,
    get_subscriber_count,
    send_test_post,
    broadcast_message,
    get_content_for_today,
)

# ============================================================
# LOGGING SETUP
# ============================================================

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format=LOG_FORMAT,
)
logger = logging.getLogger(__name__)


# ============================================================
# COMMAND HANDLERS
# ============================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command - welcome message with menu."""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    logger.info(f"/start from user {user.id} (@{user.username}) in chat {chat_id}")
    
    # Create inline keyboard menu
    keyboard = [
        [
            InlineKeyboardButton("📝 IELTS", callback_data="ielts"),
            InlineKeyboardButton("🏥 OET", callback_data="oet"),
        ],
        [
            InlineKeyboardButton("🩺 OSCE", callback_data="osce"),
            InlineKeyboardButton("🏥 NHS", callback_data="nhs"),
        ],
        [
            InlineKeyboardButton("🎯 Daily Quiz", callback_data="quiz"),
            InlineKeyboardButton("📖 Vocabulary", callback_data="vocab"),
        ],
        [
            InlineKeyboardButton("💡 Study Tips", callback_data="tips"),
            InlineKeyboardButton("🧮 Band Calculator", callback_data="calc"),
        ],
        [
            InlineKeyboardButton("📅 Study Plan", callback_data="studyplan"),
            InlineKeyboardButton("📋 Help", callback_data="help"),
        ],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = get_welcome_message(user.first_name)
    
    await update.message.reply_text(
        welcome_text,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
        disable_web_page_preview=False,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command."""
    await update.message.reply_text(
        get_help_message(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


async def ielts_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /ielts command."""
    await update.message.reply_text(
        get_ielts_resources(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


async def oet_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /oet command."""
    await update.message.reply_text(
        get_oet_resources(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


async def osce_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /osce command."""
    await update.message.reply_text(
        get_osce_resources(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


async def nhs_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /nhs command."""
    await update.message.reply_text(
        get_nhs_resources(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


# ============================================================
# QUIZ SYSTEM
# ============================================================

# Store active quiz state: chat_id -> {"question": QuizQuestion, "options": list, "correct": int}
_active_quizzes: dict[int, dict] = {}


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /quiz command - send a quiz question."""
    if not ENABLE_QUIZ:
        await update.message.reply_text("❌ Quiz feature is currently disabled.")
        return
    
    chat_id = update.effective_chat.id
    
    # Get a random question
    question, options, correct = get_random_question(chat_id)
    
    # Store quiz state
    _active_quizzes[chat_id] = {
        "question": question,
        "options": options,
        "correct": correct,
    }
    
    # Send the question
    question_text = format_question(question, options)
    
    # Create answer buttons
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data="quiz_A"),
            InlineKeyboardButton("B", callback_data="quiz_B"),
            InlineKeyboardButton("C", callback_data="quiz_C"),
            InlineKeyboardButton("D", callback_data="quiz_D"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        question_text,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
    )


async def handle_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle quiz answer button clicks."""
    query = update.callback_query
    await query.answer()
    
    chat_id = update.effective_chat.id
    data = query.data  # e.g., "quiz_A"
    
    if chat_id not in _active_quizzes:
        await query.edit_message_text(
            "❌ This quiz has expired. Start a new one with /quiz",
            parse_mode=ParseMode.HTML,
        )
        return
    
    quiz_state = _active_quizzes[chat_id]
    question = quiz_state["question"]
    options = quiz_state["options"]
    correct = quiz_state["correct"]
    
    # Extract answer letter
    answer_letter = data.split("_")[1]  # "A", "B", "C", or "D"
    
    # Format answer feedback
    answer_text = format_answer(question, answer_letter, correct, options)
    
    # Add "Next Question" button
    keyboard = [[InlineKeyboardButton("🎯 Next Question", callback_data="next_quiz")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        answer_text,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
    )
    
    # Clear quiz state
    del _active_quizzes[chat_id]


async def next_quiz_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle 'Next Question' button click."""
    query = update.callback_query
    await query.answer()
    
    # Trigger a new quiz question
    chat_id = update.effective_chat.id
    
    question, options, correct = get_random_question(chat_id)
    _active_quizzes[chat_id] = {
        "question": question,
        "options": options,
        "correct": correct,
    }
    
    question_text = format_question(question, options)
    
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data="quiz_A"),
            InlineKeyboardButton("B", callback_data="quiz_B"),
            InlineKeyboardButton("C", callback_data="quiz_C"),
            InlineKeyboardButton("D", callback_data="quiz_D"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        question_text,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
    )


# ============================================================
# VOCABULARY COMMAND
# ============================================================

async def vocab_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /vocab command - daily vocabulary word."""
    await update.message.reply_text(
        get_daily_vocab(count=1),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


# ============================================================
# TIPS COMMAND
# ============================================================

async def tips_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /tips command - 3 random study tips."""
    await update.message.reply_text(
        get_study_tips(count=3),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


# ============================================================
# CALCULATOR COMMAND
# ============================================================

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /calc command - IELTS band score calculator."""
    if not ENABLE_CALCULATOR:
        await update.message.reply_text("❌ Calculator is currently disabled.")
        return
    
    args = context.args
    
    if len(args) != 4:
        await update.message.reply_text(
            "🧮 <b>IELTS Band Score Calculator</b>\n\n"
            "<b>Usage:</b> /calc [Listening] [Reading] [Writing] [Speaking]\n\n"
            "<b>Example:</b>\n"
            "• /calc 7.0 6.5 7.5 8.0\n"
            "• /calc 8.0 7.5 7.0 7.5\n\n"
            "💡 Enter your scores for all 4 sections (0.0 - 9.0)",
            parse_mode=ParseMode.HTML,
        )
        return
    
    try:
        listening = float(args[0])
        reading = float(args[1])
        writing = float(args[2])
        speaking = float(args[3])
    except ValueError:
        await update.message.reply_text(
            "❌ Invalid input. Please enter numbers only.\n\n"
            "<b>Example:</b> /calc 7.0 6.5 7.5 8.0",
            parse_mode=ParseMode.HTML,
        )
        return
    
    result = calculate_ielts_band(listening, reading, writing, speaking)
    
    await update.message.reply_text(
        result,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


# ============================================================
# STUDY PLAN COMMAND
# ============================================================

async def studyplan_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /studyplan command - generate personalized study plan."""
    if not ENABLE_STUDY_PLAN:
        await update.message.reply_text("❌ Study plan feature is currently disabled.")
        return
    
    args = context.args
    
    if len(args) != 1:
        await update.message.reply_text(
            "📅 <b>Personalized Study Plan Generator</b>\n\n"
            "<b>Usage:</b> /studyplan [number of weeks]\n\n"
            "<b>Examples:</b>\n"
            "• /studyplan 4 — Crash plan (1 month)\n"
            "• /studyplan 8 — Standard plan (2 months)\n"
            "• /studyplan 12 — Comprehensive plan (3 months)\n"
            "• /studyplan 24 — Mastery plan (6 months)\n\n"
            "💡 Recommend 8-12 weeks for most students",
            parse_mode=ParseMode.HTML,
        )
        return
    
    try:
        weeks = int(args[0])
    except ValueError:
        await update.message.reply_text(
            "❌ Please enter a valid number of weeks.\n"
            "<b>Example:</b> /studyplan 8",
            parse_mode=ParseMode.HTML,
        )
        return
    
    plan = generate_study_plan(weeks)
    
    await update.message.reply_text(
        plan,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
    )


# ============================================================
# SUBSCRIPTION COMMANDS
# ============================================================

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /subscribe command."""
    if not ENABLE_SUBSCRIPTION:
        await update.message.reply_text("❌ Subscription feature is currently disabled.")
        return
    
    chat_id = update.effective_chat.id
    user = update.effective_user
    
    # Handle groups differently
    if update.effective_chat.type in ["group", "supergroup"]:
        # In groups, add the group itself as a subscriber
        added = add_subscriber(chat_id)
    else:
        added = add_subscriber(chat_id)
    
    if added:
        await update.message.reply_text(
            "✅ <b>Subscribed successfully!</b>\n\n"
            "📬 You'll receive daily study content every morning:\n"
            "• Monday: IELTS vocabulary (3 words)\n"
            "• Tuesday: OET speaking tips\n"
            "• Wednesday: OSCE station focus\n"
            "• Thursday: AI prompt of the day\n"
            "• Friday: NHS value of the week\n"
            "• Saturday: Study motivation\n"
            "• Sunday: Weekly challenge\n\n"
            "⏰ Posts arrive at 9:00 AM UTC\n"
            "🛑 Use /unsubscribe to stop anytime.",
            parse_mode=ParseMode.HTML,
        )
        logger.info(f"New subscription: chat_id={chat_id}, user={user.id}")
    else:
        await update.message.reply_text(
            "📬 You're already subscribed!\n\n"
            "Use /unsubscribe if you want to stop receiving daily tips.",
            parse_mode=ParseMode.HTML,
        )


async def unsubscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /unsubscribe command."""
    if not ENABLE_SUBSCRIPTION:
        await update.message.reply_text("❌ Subscription feature is currently disabled.")
        return
    
    chat_id = update.effective_chat.id
    
    removed = remove_subscriber(chat_id)
    
    if removed:
        await update.message.reply_text(
            "🛑 <b>Unsubscribed successfully.</b>\n\n"
            "You won't receive daily study tips anymore.\n\n"
            "💡 You can always re-subscribe with /subscribe\n"
            "📚 Bot commands still work anytime!",
            parse_mode=ParseMode.HTML,
        )
        logger.info(f"Unsubscribed: chat_id={chat_id}")
    else:
        await update.message.reply_text(
            "❓ You're not currently subscribed.\n\n"
            "Use /subscribe to get daily study tips!",
            parse_mode=ParseMode.HTML,
        )


# ============================================================
# ADMIN COMMANDS
# ============================================================

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /stats command (admin only)."""
    user_id = update.effective_user.id
    
    if ADMIN_IDS and user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ This command is for admins only.")
        return
    
    subscriber_count = get_subscriber_count()
    
    stats_text = (
        f"📊 <b>Bot Statistics</b>\n\n"
        f"👥 <b>Subscribers:</b> {subscriber_count}\n"
        f"🤖 <b>Bot:</b> {BOT_NAME} v{BOT_VERSION}\n"
        f"📚 <b>Quiz Database:</b> 100+ questions\n"
        f"📝 <b>Vocabulary:</b> 300+ words\n\n"
        f"🔧 <b>Features:</b>\n"
        f"• Quiz: {'✅' if ENABLE_QUIZ else '❌'}\n"
        f"• Study Plan: {'✅' if ENABLE_STUDY_PLAN else '❌'}\n"
        f"• Calculator: {'✅' if ENABLE_CALCULATOR else '❌'}\n"
        f"• Auto-posts: {'✅' if ENABLE_SUBSCRIPTION else '❌'}\n"
    )
    
    await update.message.reply_text(
        stats_text,
        parse_mode=ParseMode.HTML,
    )


async def testpost_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /testpost command (admin only) - send a test daily post."""
    user_id = update.effective_user.id
    
    if ADMIN_IDS and user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ This command is for admins only.")
        return
    
    chat_id = update.effective_chat.id
    await send_test_post(context, chat_id)


async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /broadcast command (admin only)."""
    user_id = update.effective_user.id
    
    if ADMIN_IDS and user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ This command is for admins only.")
        return
    
    if not context.args:
        await update.message.reply_text(
            "📢 <b>Broadcast Message</b>\n\n"
            "Usage: /broadcast Your message here\n\n"
            "Sends your message to all subscribers.",
            parse_mode=ParseMode.HTML,
        )
        return
    
    message = " ".join(context.args)
    # Allow HTML in broadcast
    message = f"📢 <b>Announcement</b>\n\n{message}"
    
    await update.message.reply_text("📢 Broadcasting...")
    await broadcast_message(context, message, user_id)


# ============================================================
# CALLBACK QUERY HANDLER
# ============================================================

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle inline button callbacks."""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    chat_id = update.effective_chat.id
    
    # Handle quiz answers
    if data.startswith("quiz_"):
        await handle_quiz_answer(update, context)
        return
    
    # Handle next quiz
    if data == "next_quiz":
        await next_quiz_handler(update, context)
        return
    
    # Handle menu callbacks
    if data == "ielts":
        await query.edit_message_text(
            get_ielts_resources(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )
    elif data == "oet":
        await query.edit_message_text(
            get_oet_resources(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )
    elif data == "osce":
        await query.edit_message_text(
            get_osce_resources(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )
    elif data == "nhs":
        await query.edit_message_text(
            get_nhs_resources(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )
    elif data == "quiz":
        # Start a new quiz
        question, options, correct = get_random_question(chat_id)
        _active_quizzes[chat_id] = {
            "question": question,
            "options": options,
            "correct": correct,
        }
        
        question_text = format_question(question, options)
        
        keyboard = [
            [
                InlineKeyboardButton("A", callback_data="quiz_A"),
                InlineKeyboardButton("B", callback_data="quiz_B"),
                InlineKeyboardButton("C", callback_data="quiz_C"),
                InlineKeyboardButton("D", callback_data="quiz_D"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            question_text,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
        )
    elif data == "vocab":
        await query.edit_message_text(
            get_daily_vocab(count=1),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )
    elif data == "tips":
        await query.edit_message_text(
            get_study_tips(count=3),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )
    elif data == "calc":
        await query.edit_message_text(
            "🧮 <b>IELTS Band Score Calculator</b>\n\n"
            "<b>Usage:</b> /calc [Listening] [Reading] [Writing] [Speaking]\n\n"
            "<b>Example:</b> /calc 7.0 6.5 7.5 8.0\n\n"
            "💡 Enter your scores for all 4 sections (0.0 - 9.0)",
            parse_mode=ParseMode.HTML,
        )
    elif data == "studyplan":
        await query.edit_message_text(
            "📅 <b>Study Plan Generator</b>\n\n"
            "<b>Usage:</b> /studyplan [number of weeks]\n\n"
            "<b>Examples:</b>\n"
            "• /studyplan 4 — Crash plan\n"
            "• /studyplan 8 — Standard plan\n"
            "• /studyplan 12 — Comprehensive plan\n\n"
            "💡 Recommend 8-12 weeks for most students",
            parse_mode=ParseMode.HTML,
        )
    elif data == "help":
        await query.edit_message_text(
            get_help_message(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )


# ============================================================
# GROUP CHAT HANDLER
# ============================================================

async def group_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages in groups - respond to mentions and relevant keywords."""
    if not update.message or not update.message.text:
        return
    
    text = update.message.text.lower()
    bot_username = context.bot.username.lower()
    
    # Check if bot is mentioned
    if f"@{bot_username}" in text:
        # Bot was mentioned - provide help
        await update.message.reply_text(
            f"👋 Hi! I'm <b>{BOT_NAME}</b>.\n\n"
            f"Use these commands in this group:\n"
            f"• /ielts — IELTS resources\n"
            f"• /oet — OET resources\n"
            f"• /osce — OSCE resources\n"
            f"• /quiz — Daily quiz\n"
            f"• /vocab — Vocabulary word\n"
            f"• /tips — Study tips\n"
            f"• /nhs — NHS resources\n"
            f"• /calc — Band calculator\n"
            f"• /help — All commands\n\n"
            f"📚 DM me for a personalized experience!",
            parse_mode=ParseMode.HTML,
        )
        return
    
    # Auto-respond to study-related keywords (subtle, not spammy)
    study_keywords = {
        "ielts": get_ielts_resources,
        "oet exam": get_oet_resources,
        "osce prep": get_osce_resources,
        "nhs interview": get_nhs_resources,
    }
    
    # Only respond occasionally in groups (5% chance) to avoid being annoying
    import random
    if random.random() < 0.05:
        for keyword, func in study_keywords.items():
            if keyword in text:
                # Check if bot was recently active in this group (avoid spam)
                chat_id = update.effective_chat.id
                last_active = context.chat_data.get("last_auto_response", 0) if context.chat_data else 0
                from time import time as get_time
                
                if get_time() - last_active > 3600:  # Only once per hour max
                    await update.message.reply_text(
                        func(),
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=False,
                    )
                    if context.chat_data is not None:
                        context.chat_data["last_auto_response"] = get_time()
                break


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    logger.error(f"Update {update} caused error: {context.error}", exc_info=context.error)
    
    # Notify user if possible
    if update and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Oops! Something went wrong. Please try again.\n"
                "If the problem persists, contact support.",
                parse_mode=ParseMode.HTML,
            )
        except Exception:
            pass


# ============================================================
# MAIN APPLICATION
# ============================================================

def main() -> None:
    """Start the bot."""
    # Check token
    token = BOT_TOKEN
    if not token or token == "YOUR_BOT_TOKEN_HERE":
        logger.error("❌ BOT_TOKEN not set! Please set the BOT_TOKEN environment variable.")
        print("\n" + "=" * 60)
        print("ERROR: BOT_TOKEN not configured!")
        print("=" * 60)
        print("\nTo set your token:")
        print("  1. Get a token from @BotFather on Telegram")
        print("  2. Set environment variable: export BOT_TOKEN='your_token'")
        print("  3. Or edit config.py and set BOT_TOKEN directly\n")
        sys.exit(1)
    
    logger.info(f"🚀 Starting {BOT_NAME} v{BOT_VERSION}...")
    
    # Build application
    application = (
        Application.builder()
        .token(token)
        .build()
    )
    
    # ============================================================
    # REGISTER COMMAND HANDLERS
    # ============================================================
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ielts", ielts_command))
    application.add_handler(CommandHandler("oet", oet_command))
    application.add_handler(CommandHandler("osce", osce_command))
    application.add_handler(CommandHandler("nhs", nhs_command))
    application.add_handler(CommandHandler("quiz", quiz_command))
    application.add_handler(CommandHandler("vocab", vocab_command))
    application.add_handler(CommandHandler("tips", tips_command))
    application.add_handler(CommandHandler("calc", calc_command))
    application.add_handler(CommandHandler("studyplan", studyplan_command))
    application.add_handler(CommandHandler("subscribe", subscribe_command))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe_command))
    
    # Admin commands
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("testpost", testpost_command))
    application.add_handler(CommandHandler("broadcast", broadcast_command))
    
    # Callback queries (inline buttons)
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Group message handler
    application.add_handler(
        MessageHandler(filters.ChatType.GROUPS | filters.ChatType.SUPERGROUP, group_message_handler)
    )
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # ============================================================
    # SETUP SCHEDULER
    # ============================================================
    
    setup_scheduler(application)
    
    # ============================================================
    # START BOT
    # ============================================================
    
    logger.info(f"✅ {BOT_NAME} is running! Press Ctrl+C to stop.")
    logger.info(f"📊 Subscribers: {get_subscriber_count()}")
    
    # Run the bot until interrupted
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
