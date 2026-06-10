# AngloTec Study Bot

A helpful Discord bot that autonomously assists people preparing for IELTS, OET, OSCE, PLAB, and NHS interviews — providing genuine value first, with subtle links to free AngloTec tools.

---

## What This Bot Does

- **Monitors conversations** for study-related keywords and offers helpful advice
- **Responds to commands** for IELTS, OET, OSCE, NHS resources, calculators, tips, timers, and AI prompts
- **Provides genuine help first** — never spammy, always useful
- **Includes subtle tool links** only when genuinely relevant
- **Follows anti-spam rules**: max 3 responses/hour per channel, 30-120s delays, 1-in-5 response rate

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a Discord Bot Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** and give it a name
3. Go to the **Bot** tab on the left
4. Click **Add Bot**
5. Under **Privileged Gateway Intents**, enable:
   - **Message Content Intent** (required for keyword monitoring)
   - **Server Members Intent**
6. Click **Reset Token** and copy the new token

### 3. Set Your Bot Token

**Option A — Environment Variable (Recommended):**
```bash
export DISCORD_BOT_TOKEN=your_token_here
python bot.py
```

**Option B — Edit config.py:**
```python
BOT_TOKEN = "your_token_here"  # Replace in config.py
```

### 4. Invite the Bot to Your Server

1. In the Developer Portal, go to **OAuth2 > URL Generator**
2. Under **Scopes**, check `bot`
3. Under **Bot Permissions**, check:
   - Send Messages
   - Read Messages/View Channels
   - Read Message History
   - Embed Links
   - Add Reactions
   - Use Slash Commands (optional)
4. Copy the generated URL and open it in your browser
5. Select your server and authorise

### 5. Run the Bot

```bash
python bot.py
```

You should see:
```
AngloTec Study Bot is online!
Connected to X server(s)
```

---

## Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `!help` | Show all available commands | `!help` |
| `!ielts` | IELTS resources & links | `!ielts` |
| `!oet` | OET resources & links | `!oet` |
| `!osce` | OSCE resources & PLAB tips | `!osce` |
| `!nhs` | NHS interview resources | `!nhs` |
| `!calc <L> <R> <W> <S>` | Calculate IELTS band score | `!calc 7.5 8.0 6.5 7.0` |
| `!tips ielts` | Get 5 random IELTS tips | `!tips ielts` |
| `!tips oet` | Get 5 random OET tips | `!tips oet` |
| `!timer <minutes>` | Set a study timer | `!timer 25` |
| `!prompt <category>` | Generate an AI study prompt | `!prompt osce` |
| `!ping` | Check bot latency | `!ping` |

---

## File Structure

```
discord-bot/
├── bot.py              # Main Discord bot (commands + autonomous monitoring)
├── responses.py        # Database of 100+ keyword-triggered responses
├── config.py           # All configuration settings
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── bot.log             # Activity log (created when bot runs)
```

---

## Configuration

Edit `config.py` to customise the bot:

```python
# Response frequency (higher = less frequent)
RESPONSE_CHANCE = 5              # 1 in 5 messages
MIN_RESPONSE_DELAY = 30          # Minimum seconds before responding
MAX_RESPONSE_DELAY = 120         # Maximum seconds before responding
MAX_RESPONSES_PER_CHANNEL_PER_HOUR = 3
CHANNEL_COOLDOWN_SECONDS = 600   # 10 minutes between responses

# Restrict to specific channels (empty = all channels)
ALLOWED_CHANNEL_IDS = []         # e.g., [123456789, 987654321]

# Admin users (for !stats command)
ADMIN_USER_IDS = []              # e.g., [123456789]

# Tool links (update these to your actual URLs)
TOOL_LINKS = {
    "ielts_calculator": "https://anglotec.co.uk/ielts-band-score-calculator",
    ...
}
```

---

## Autonomous Behaviour

The bot monitors all messages for keywords like "IELTS", "OET", "OSCE", "PLAB", "NHS", etc.

**Example interactions:**

| User Says | Bot Responds With |
|-----------|-------------------|
| "I'm worried about my IELTS speaking" | Speaking tips + link to Speaking Practice |
| "How do I prepare for OET writing?" | Writing guide + link to OET Checklist |
| "PLAB 2 OSCE is so hard" | Encouragement + link to OSCE Generator |
| "NHS interview next week" | Interview tips + link to Interview Bank |

**Anti-spam rules in effect:**
- Only responds to 1 in 5 qualifying messages
- Waits 30-120 seconds before responding (appears human)
- Max 3 responses per channel per hour
- 10-minute cooldown between responses in the same channel

---

## Response Database

The `responses.py` file contains **100+ keyword-triggered responses** across:

- **IELTS Speaking** (15 responses)
- **IELTS Writing** (15 responses)
- **IELTS Reading** (10 responses)
- **IELTS Listening** (8 responses)
- **IELTS General** (8 responses)
- **OET Writing** (8 responses)
- **OET Speaking/Roleplay** (8 responses)
- **OET Reading & Listening** (4 responses)
- **OSCE / PLAB** (10 responses)
- **NHS / Interview** (10 responses)
- **General / Motivational** (10 responses)

Plus:
- 20 IELTS tips
- 20 OET tips
- 25 AI prompts (5 per category)

---

## Running on a Server (24/7)

### Using systemd (Linux)

Create a service file:
```bash
sudo nano /etc/systemd/system/anglotec-bot.service
```

Add:
```ini
[Unit]
Description=AngloTec Study Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/discord-bot
Environment=DISCORD_BOT_TOKEN=your_token_here
ExecStart=/path/to/python bot.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable anglotec-bot
sudo systemctl start anglotec-bot
sudo systemctl status anglotec-bot
```

### Using Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

Build and run:
```bash
docker build -t anglotec-bot .
docker run -e DISCORD_BOT_TOKEN=your_token_here anglotec-bot
```

### Using PM2 (Node.js-style process manager)

```bash
pm2 start bot.py --name anglotec-bot --interpreter python3
pm2 save
pm2 startup
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "DISCORD BOT TOKEN NOT SET!" | Set the `DISCORD_BOT_TOKEN` environment variable or edit `config.py` |
| "Failed to login" | Your token is invalid — reset it in the Discord Developer Portal |
| Bot doesn't respond to messages | Check that **Message Content Intent** is enabled in the Developer Portal |
| Bot responds to every message | Check `RESPONSE_CHANCE` in config.py (default: 5 = 1 in 5) |
| Bot won't join a server | Regenerate the invite link with correct permissions |

---

## Adding Custom Responses

Edit `responses.py` and add entries to the `RESPONSES` list:

```python
{
    "keywords": ["your keyword", "another keyword"],
    "response": "Your helpful response text here...",
    "category": "ielts",  # or oet, osce, nhs, general
    "link_key": "ielts_calculator",  # optional — must match a key in TOOL_LINKS
    "link_text": "Check out this free tool: {link}",  # optional — {link} gets replaced
},
```

Restart the bot for changes to take effect.

---

## Logging

All bot activity is logged to `bot.log` and the console. Check this file for:
- Keyword matches and responses sent
- Errors and warnings
- Server join/leave events

---

## License

This bot is built for AngloTec. Modify and use as needed for your study community.
