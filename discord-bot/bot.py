"""
AngloTec Study Bot - Main Discord Bot
======================================
A helpful study companion for IELTS, OET, OSCE, PLAB, and NHS preparation.
Autonomous keyword monitoring with genuine help first, subtle links second.

Setup:
1. Set DISCORD_BOT_TOKEN environment variable
2. pip install -r requirements.txt
3. python bot.py
"""

import asyncio
import logging
import os
import random
import time
from collections import defaultdict
from datetime import datetime, timedelta

import discord
from discord.ext import commands, tasks

from config import (
    ADMIN_USER_IDS,
    ALLOWED_CHANNEL_IDS,
    ALLOWED_GUILD_IDS,
    BOT_ACTIVITY,
    BOT_DESCRIPTION,
    BOT_NAME,
    BOT_PREFIX,
    BOT_TOKEN,
    CHANNEL_COOLDOWN_SECONDS,
    LOG_FILE,
    LOG_LEVEL,
    MAX_RESPONSES_PER_CHANNEL_PER_HOUR,
    MAX_RESPONSE_DELAY,
    MIN_RESPONSE_DELAY,
    RESPONSE_CHANCE,
)
from responses import (
    calculate_ielts_band,
    find_response,
    format_response,
    get_ai_prompt,
    get_random_tips,
    get_resource_message,
)

# ── Logging Setup ────────────────────────────────────────────────────────────
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(BOT_NAME)

# ── Rate Limiting Trackers ──────────────────────────────────────────────────
# Track responses per channel for hourly limit
channel_response_times = defaultdict(list)  # channel_id -> [timestamp, ...]
# Track last response time per channel for cooldown
channel_last_response = {}  # channel_id -> timestamp
# Track message count per channel for RESPONSE_CHANCE
channel_message_counts = defaultdict(int)  # channel_id -> count


# ── Bot Intents ──────────────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.members = True


# ── Bot Instance ─────────────────────────────────────────────────────────────
class AngloTecStudyBot(commands.Bot):
    """AngloTec Study Bot - Helpful study companion for healthcare professionals."""

    def __init__(self):
        super().__init__(
            command_prefix=BOT_PREFIX,
            intents=intents,
            description=BOT_DESCRIPTION,
            help_command=None,  # We'll use a custom help command
        )

    async def setup_hook(self):
        """Called when the bot starts."""
        logger.info("Bot is starting up...")

    async def on_ready(self):
        """Called when the bot is ready and connected."""
        logger.info(f"{BOT_NAME} is online!")
        logger.info(f"Connected to {len(self.guilds)} server(s)")
        for guild in self.guilds:
            logger.info(f"  - {guild.name} (ID: {guild.id})")

        # Set bot activity status
        activity = discord.Activity(
            type=discord.ActivityType.listening,
            name=BOT_ACTIVITY,
        )
        await self.change_presence(activity=activity)

        # Start background tasks
        self.cleanup_old_data.start()

    async def on_command_error(self, ctx, error):
        """Handle command errors gracefully."""
        if isinstance(error, commands.CommandNotFound):
            return  # Ignore unknown commands silently

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Looks like you're missing some info! Try `!help` to see how to use this command."
            )
            return

        if isinstance(error, commands.BadArgument):
            await ctx.send(
                f"I couldn't understand one of your inputs. Check `!help` for the correct format!"
            )
            return

        logger.error(f"Command error in {ctx.command}: {error}")

    @tasks.loop(hours=1)
    async def cleanup_old_data(self):
        """Clean up old rate limiting data every hour."""
        now = datetime.now()
        cutoff = now - timedelta(hours=1)

        cleaned_channels = 0
        for channel_id in list(channel_response_times.keys()):
            old_times = channel_response_times[channel_id]
            channel_response_times[channel_id] = [
                t for t in old_times if t > cutoff
            ]
            if not channel_response_times[channel_id]:
                del channel_response_times[channel_id]
                cleaned_channels += 1

        if cleaned_channels > 0:
            logger.info(f"Cleaned up rate limit data for {cleaned_channels} channels")


bot = AngloTecStudyBot()


# ═══════════════════════════════════════════════════════════════════════════════
# AUTONOMOUS KEYWORD MONITORING
# ═══════════════════════════════════════════════════════════════════════════════

@bot.event
async def on_message(message):
    """
    Monitor messages for keywords and respond autonomously.
    This is the core 'autonomous help' feature.
    """
    # Don't respond to own messages
    if message.author == bot.user:
        return

    # Don't respond to other bots
    if message.author.bot:
        return

    # Check if we're in an allowed channel (if configured)
    if ALLOWED_CHANNEL_IDS and message.channel.id not in ALLOWED_CHANNEL_IDS:
        return

    # Check if we're in an allowed guild (if configured)
    if ALLOWED_GUILD_IDS and message.guild and message.guild.id not in ALLOWED_GUILD_IDS:
        return

    # Don't respond to command messages (they're handled separately)
    if message.content.startswith(BOT_PREFIX):
        await bot.process_commands(message)
        return

    # ── Rate Limiting Logic ─────────────────────────────────────────────────
    channel_id = message.channel.id
    now = datetime.now()

    # Check hourly limit
    hour_ago = now - timedelta(hours=1)
    recent_responses = [
        t for t in channel_response_times.get(channel_id, []) if t > hour_ago
    ]

    if len(recent_responses) >= MAX_RESPONSES_PER_CHANNEL_PER_HOUR:
        await bot.process_commands(message)
        return

    # Check cooldown since last response
    last_resp_time = channel_last_response.get(channel_id)
    if last_resp_time and (now - last_resp_time).total_seconds() < CHANNEL_COOLDOWN_SECONDS:
        await bot.process_commands(message)
        return

    # 1-in-N chance to respond (looks natural, not spammy)
    channel_message_counts[channel_id] += 1
    if channel_message_counts[channel_id] % RESPONSE_CHANCE != 0:
        await bot.process_commands(message)
        return

    # ── Keyword Matching ────────────────────────────────────────────────────
    response_data = find_response(message.content)

    if not response_data:
        await bot.process_commands(message)
        return

    # ── Send Response ───────────────────────────────────────────────────────
    # Add random delay to seem human (30-120 seconds)
    delay = random.randint(MIN_RESPONSE_DELAY, MAX_RESPONSE_DELAY)
    logger.info(
        f"Keyword match in #{message.channel.name} ({message.guild.name if message.guild else 'DM'}). "
        f"Responding in {delay}s to: '{message.content[:80]}...'"
    )

    await asyncio.sleep(delay)

    # Re-check limits after delay (in case another response was sent)
    recent_responses = [
        t for t in channel_response_times.get(channel_id, []) if t > hour_ago
    ]
    if len(recent_responses) >= MAX_RESPONSES_PER_CHANNEL_PER_HOUR:
        return

    last_resp_time = channel_last_response.get(channel_id)
    if last_resp_time and (datetime.now() - last_resp_time).total_seconds() < CHANNEL_COOLDOWN_SECONDS:
        return

    # Format and send the response
    formatted = format_response(response_data)

    # Send as a reply to the original message
    try:
        await message.reply(formatted, mention_author=False)

        # Update rate limit trackers
        channel_response_times[channel_id].append(datetime.now())
        channel_last_response[channel_id] = datetime.now()

        logger.info(f"Responded in #{message.channel.name}: category={response_data['category']}")

    except discord.Forbidden:
        logger.warning(f"Forbidden to reply in #{message.channel.name}")
    except discord.HTTPException as e:
        logger.error(f"Failed to send message: {e}")

    # Still process commands (in case message was also a command)
    await bot.process_commands(message)


# ═══════════════════════════════════════════════════════════════════════════════
# BOT COMMANDS
# ═══════════════════════════════════════════════════════════════════════════════

@bot.command(name="help")
async def help_command(ctx):
    """Show all available commands."""
    embed = discord.Embed(
        title="📚 AngloTec Study Bot — Commands",
        description="Your study companion for IELTS, OET, OSCE, PLAB & NHS prep!",
        color=0x3498db,
    )

    embed.add_field(
        name="📝 Study Resources",
        value=(
            "`!ielts` — IELTS resources & calculator\n"
            "`!oet` — OET resources & checklists\n"
            "`!osce` — OSCE scenarios & PLAB tips\n"
            "`!nhs` — NHS interview resources"
        ),
        inline=False,
    )

    embed.add_field(
        name="🧮 Tools",
        value=(
            "`!calc <L> <R> <W> <S>` — Calculate IELTS band score\n"
            "  Example: `!calc 7.5 8.0 6.5 7.0`\n"
            "`!timer <minutes>` — Set a study timer\n"
            "  Example: `!timer 25`"
        ),
        inline=False,
    )

    embed.add_field(
        name="💡 Study Tips",
        value=(
            "`!tips ielts` — 5 random IELTS tips\n"
            "`!tips oet` — 5 random OET tips"
        ),
        inline=False,
    )

    embed.add_field(
        name="🤖 AI Prompts",
        value=(
            "`!prompt ielts` — Generate IELTS study prompts\n"
            "`!prompt oet` — Generate OET study prompts\n"
            "`!prompt osce` — Generate OSCE practice scenarios\n"
            "`!prompt nhs` — Generate NHS interview prep prompts\n"
            "`!prompt general` — Generate general study prompts"
        ),
        inline=False,
    )

    embed.add_field(
        name="🤝 How I Help",
        value=(
            "I also monitor conversations and offer help when I see keywords like "
            "'IELTS', 'OET', 'OSCE', 'PLAB', 'NHS', etc. Just chat naturally and I might jump in with tips!"
        ),
        inline=False,
    )

    embed.set_footer(text="Type any command to get started. Good luck with your studies!")

    await ctx.send(embed=embed)


@bot.command(name="ielts")
async def ielts_command(ctx):
    """Show IELTS resources and calculator link."""
    msg = get_resource_message("ielts")
    await ctx.send(msg)


@bot.command(name="oet")
async def oet_command(ctx):
    """Show OET resources and role-play generator link."""
    msg = get_resource_message("oet")
    await ctx.send(msg)


@bot.command(name="osce")
async def osce_command(ctx):
    """Show OSCE resources and scenario generator link."""
    msg = get_resource_message("osce")
    await ctx.send(msg)


@bot.command(name="nhs")
async def nhs_command(ctx):
    """Show NHS interview resources and interview bank link."""
    msg = get_resource_message("nhs")
    await ctx.send(msg)


@bot.command(name="calc")
async def calc_command(ctx, listening: str, reading: str, writing: str, speaking: str):
    """
    Calculate IELTS band score from 4 section scores.
    Usage: !calc 7.5 8.0 6.5 7.0
    """
    try:
        # Parse scores (handle both comma and dot decimals)
        scores = [listening, reading, writing, speaking]
        parsed_scores = []
        for s in scores:
            s = s.replace(",", ".")
            parsed_scores.append(float(s))

        l, r, w, s_score = parsed_scores

        # Validate score range
        for score, name in zip(parsed_scores, ["Listening", "Reading", "Writing", "Speaking"]):
            if score < 0 or score > 9:
                await ctx.send(
                    f"Your {name} score ({score}) doesn't look right. IELTS scores range from 0 to 9. "
                    f"Try again like: `!calc 7.5 8.0 6.5 7.0`"
                )
                return

        # Calculate
        result = calculate_ielts_band(l, r, w, s_score)

        # Create embed
        embed = discord.Embed(
            title="🎯 IELTS Band Score Calculator",
            color=0x2ecc71 if result["overall"] >= 7.0 else 0xf39c12 if result["overall"] >= 6.0 else 0xe74c3c,
        )

        embed.add_field(name="Listening", value=f"{result['listening']}", inline=True)
        embed.add_field(name="Reading", value=f"{result['reading']}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)  # Spacer
        embed.add_field(name="Writing", value=f"{result['writing']}", inline=True)
        embed.add_field(name="Speaking", value=f"{result['speaking']}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)  # Spacer

        embed.add_field(
            name="Average",
            value=f"{result['average']}",
            inline=True,
        )
        embed.add_field(
            name="Overall Band",
            value=f"**{result['overall']}**",
            inline=True,
        )
        embed.add_field(name="\u200b", value="\u200b", inline=True)  # Spacer

        # Add NMC eligibility note
        if result["overall"] >= 7.0 and all(score >= 6.5 for score in [l, r, w, s_score]):
            embed.add_field(
                name="✅ NMC Eligibility",
                value="You meet the NMC's IELTS requirements! (7.0 overall, minimum 6.5 in Writing, 7.0 in others)",
                inline=False,
            )
        elif result["overall"] >= 6.5:
            embed.add_field(
                name="⚠️ NMC Note",
                value=(
                    "For NMC registration, you need: 7.0 overall with minimum 7.0 in Listening, Reading, Speaking "
                    "and 6.5 in Writing (all from a single test). Keep practising!"
                ),
                inline=False,
            )
        else:
            embed.add_field(
                name="📚 Keep Studying!",
                value="You're on your way! Focus on your weakest section and keep practising.",
                inline=False,
            )

        await ctx.send(embed=embed)

    except ValueError:
        await ctx.send(
            "I couldn't understand those scores. Please use numbers like: `!calc 7.5 8.0 6.5 7.0`"
        )


@bot.command(name="tips")
async def tips_command(ctx, category: str = "ielts"):
    """
    Get random study tips.
    Usage: !tips ielts  or  !tips oet
    """
    category = category.lower().strip()

    if category not in ["ielts", "oet"]:
        await ctx.send(
            "I can give tips for `ielts` or `oet`. Try: `!tips ielts` or `!tips oet`"
        )
        return

    tips = get_random_tips(category, count=5)

    emoji = "📝" if category == "ielts" else "🏥"
    title = f"{emoji} {category.upper()} Study Tips"

    embed = discord.Embed(
        title=title,
        description="Here are 5 tips to help with your preparation:",
        color=0x9b59b6,
    )

    for i, tip in enumerate(tips, 1):
        embed.add_field(name=f"Tip #{i}", value=tip, inline=False)

    embed.set_footer(text=f"Use !tips {category} again for more tips!")

    await ctx.send(embed=embed)


@bot.command(name="timer")
async def timer_command(ctx, minutes: int = 25):
    """
    Set a study timer.
    Usage: !timer 25
    """
    if minutes < 1:
        await ctx.send("Timer needs to be at least 1 minute! Try: `!timer 25`")
        return

    if minutes > 120:
        await ctx.send("That's a long session! I'll set a 120-minute max timer for now.")
        minutes = 120

    embed = discord.Embed(
        title="⏱️ Study Timer Started",
        description=f"I'll remind you in **{minutes} minute{'s' if minutes != 1 else ''}**. Focus up!",
        color=0x1abc9c,
    )
    embed.set_footer(text="Use the Pomodoro technique: 25 min study, 5 min break!")

    message = await ctx.send(embed=embed)

    # Wait for the timer
    await asyncio.sleep(minutes * 60)

    # Timer done
    done_embed = discord.Embed(
        title="⏰ Time's Up!",
        description=f"Great work studying for {minutes} minutes! Take a well-deserved break. ☕",
        color=0xe67e22,
    )

    try:
        await ctx.send(f"{ctx.author.mention}", embed=done_embed)
    except discord.HTTPException:
        pass


@bot.command(name="prompt")
async def prompt_command(ctx, category: str = "general"):
    """
    Generate an AI prompt for study practice.
    Usage: !prompt ielts  or  !prompt oet  or  !prompt osce  or  !prompt nhs  or  !prompt general
    """
    category = category.lower().strip()

    valid_categories = ["ielts", "oet", "osce", "nhs", "general"]
    if category not in valid_categories:
        await ctx.send(
            f"I can generate prompts for: {', '.join(valid_categories)}. "
            f"Try: `!prompt ielts`"
        )
        return

    prompt_text = get_ai_prompt(category)

    if not prompt_text:
        await ctx.send("Hmm, I couldn't generate a prompt right now. Try again!")
        return

    embed = discord.Embed(
        title=f"🤖 AI Study Prompt — {category.upper()}",
        description=f"Copy and paste this into ChatGPT, Claude, or any AI tool:\n\n```\n{prompt_text}\n```",
        color=0x8e44ad,
    )

    embed.add_field(
        name="💡 How to use",
        value=(
            "1. Copy the prompt above\n"
            "2. Paste it into ChatGPT/Claude/Gemini\n"
            "3. Replace [bracketed] parts with your topic\n"
            "4. Use the generated content to practise!"
        ),
        inline=False,
    )

    embed.set_footer(text=f"Use !prompt {category} again for another prompt!")

    await ctx.send(embed=embed)


# ═══════════════════════════════════════════════════════════════════════════════
# ADMIN COMMANDS
# ═══════════════════════════════════════════════════════════════════════════════

@bot.command(name="stats")
async def stats_command(ctx):
    """Show bot statistics (admin only)."""
    if ctx.author.id not in ADMIN_USER_IDS:
        return

    embed = discord.Embed(
        title="📊 Bot Statistics",
        color=0x3498db,
    )

    embed.add_field(name="Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name="Latency", value=f"{round(bot.latency * 1000)}ms", inline=True)

    total_members = sum(g.member_count for g in bot.guilds)
    embed.add_field(name="Total Members", value=total_members, inline=True)

    # Response stats
    total_responses = sum(len(times) for times in channel_response_times.values())
    embed.add_field(name="Responses (this hour)", value=total_responses, inline=True)

    embed.add_field(name="Uptime", value="See log file for details", inline=True)

    await ctx.send(embed=embed)


@bot.command(name="ping")
async def ping_command(ctx):
    """Check bot latency."""
    latency_ms = round(bot.latency * 1000)

    emoji = "🟢" if latency_ms < 100 else "🟡" if latency_ms < 300 else "🔴"

    await ctx.send(f"{emoji} Pong! Latency: **{latency_ms}ms**")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

def validate_token():
    """Validate that the bot token is set."""
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        logger.error("=" * 60)
        logger.error("DISCORD BOT TOKEN NOT SET!")
        logger.error("=" * 60)
        logger.error("")
        logger.error("Please set your Discord bot token:")
        logger.error("")
        logger.error("  Option 1 - Environment variable:")
        logger.error("    export DISCORD_BOT_TOKEN=your_token_here")
        logger.error("")
        logger.error("  Option 2 - Edit config.py:")
        logger.error("    Change BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'")
        logger.error("")
        logger.error("Get your token from: https://discord.com/developers/applications")
        logger.error("=" * 60)
        return False
    return True


if __name__ == "__main__":
    if validate_token():
        logger.info("Starting AngloTec Study Bot...")
        try:
            bot.run(BOT_TOKEN)
        except discord.LoginFailure:
            logger.error("Failed to login. Your token may be invalid.")
            logger.error("Get a new token from: https://discord.com/developers/applications")
        except Exception as e:
            logger.error(f"Bot crashed: {e}")
    else:
        exit(1)
