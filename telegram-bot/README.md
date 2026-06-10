# AngloTec Study Bot for Telegram

> A powerful Telegram bot for IELTS, OET & OSCE exam preparation. Works in private chats and groups, providing daily study content, quizzes, vocabulary, and personalized study plans while promoting AngloTec's free tools.

## Features

| Feature | Description |
|---------|-------------|
| **12 Commands** | `/start`, `/ielts`, `/oet`, `/osce`, `/nhs`, `/quiz`, `/vocab`, `/tips`, `/calc`, `/studyplan`, `/subscribe`, `/unsubscribe` |
| **100+ Quiz Questions** | IELTS, OET, OSCE, NHS, and Vocabulary categories with explanations |
| **300+ Vocabulary Words** | With definitions, example sentences, and IELTS/OET tags |
| **Daily Auto-Posts** | Themed content every day of the week for subscribers |
| **Study Plan Generator** | Personalized plans from 1 week to 52 weeks |
| **Band Calculator** | IELTS overall band calculator with NHS requirement check |
| **Group Support** | Works in any Telegram group with @mention support |
| **Admin Tools** | Stats, broadcast, and test post commands |

## File Structure

```
telegram-bot/
├── bot.py              # Main bot with all command handlers
├── responses.py        # All responses, tips, and content generators
├── quiz.py             # Quiz database (100+ questions)
├── scheduler.py        # Daily auto-post scheduler
├── config.py           # Bot token, URLs, and settings
├── requirements.txt    # Python dependencies
├── subscribers.json    # Auto-generated subscriber database
└── README.md           # This file
```

## Quick Start

### 1. Prerequisites

- Python 3.9 or higher
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

### 2. Installation

```bash
# Clone or download the bot files
cd telegram-bot

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Set your bot token as an environment variable:

```bash
# Linux/Mac
export BOT_TOKEN="your_bot_token_here"

# Windows
set BOT_TOKEN=your_bot_token_here
```

Or edit `config.py` directly:

```python
BOT_TOKEN = "your_bot_token_here"  # Replace this
```

### 4. Run the Bot

```bash
python bot.py
```

You should see:
```
Starting AngloTec Study Bot v1.0.0...
Daily scheduler set up for 09:00 UTC.
Bot is running! Press Ctrl+C to stop.
```

## Bot Commands

### User Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Welcome message with menu | `/start` |
| `/ielts` | IELTS resources & tips | `/ielts` |
| `/oet` | OET resources & tips | `/oet` |
| `/osce` | OSCE station preparation | `/osce` |
| `/nhs` | NHS career resources | `/nhs` |
| `/quiz` | Daily IELTS/OET question | `/quiz` |
| `/vocab` | Daily vocabulary word | `/vocab` |
| `/tips` | 3 random study tips | `/tips` |
| `/calc` | IELTS band calculator | `/calc 7.0 6.5 7.5 8.0` |
| `/studyplan` | Generate study plan | `/studyplan 8` |
| `/subscribe` | Daily tips subscription | `/subscribe` |
| `/unsubscribe` | Stop daily tips | `/unsubscribe` |
| `/help` | Show all commands | `/help` |

### Admin Commands

| Command | Description |
|---------|-------------|
| `/stats` | Show bot statistics |
| `/testpost` | Send a test daily post |
| `/broadcast <msg>` | Message all subscribers |

Add your Telegram user ID to `ADMIN_IDS` in `config.py` to use admin commands.

## Daily Auto-Post Schedule

Subscribers receive themed content at 9:00 AM UTC every day:

| Day | Theme | Content |
|-----|-------|---------|
| **Monday** | IELTS Vocabulary | 3 high-value words with definitions |
| **Tuesday** | OET Speaking | Speaking tips & strategies |
| **Wednesday** | OSCE Station | Station type explanation & tips |
| **Thursday** | AI Prompt | Copy-paste AI prompts for study |
| **Friday** | NHS Value | NHS core value + interview prep |
| **Saturday** | Motivation | Inspirational quote + challenge |
| **Sunday** | Weekly Challenge | Actionable study challenge |

## Adding the Bot to Groups

1. Add the bot to any Telegram group
2. The bot works silently until mentioned
3. Users can type `@bot_username` or use `/commands`
4. The bot responds with helpful content + subtle tool promotion

**Pro tip:** Use `/subscribe` in a group to enable daily auto-posts for all members.

## Customization

### Changing AngloTec URLs

Edit `ANGLOTEC_URLS` in `config.py`:

```python
ANGLOTEC_URLS = {
    "tools": "https://your-tools-url.com",
    "ielts_calculator": "https://your-tools-url.com/ielts-calculator",
    # ... etc
}
```

### Changing Daily Post Time

Edit `DAILY_POST_TIME` in `config.py` (UTC):

```python
from datetime import time
DAILY_POST_TIME = time(hour=9, minute=0)  # 9:00 AM UTC
```

### Adding Admin IDs

```python
ADMIN_IDS = [
    123456789,  # Your Telegram user ID
    987654321,  # Another admin
]
```

### Toggle Features

```python
ENABLE_QUIZ = True          # /quiz command
ENABLE_STUDY_PLAN = True    # /studyplan command
ENABLE_CALCULATOR = True    # /calc command
ENABLE_AUTO_POSTS = True    # Daily scheduled posts
ENABLE_SUBSCRIPTION = True  # /subscribe /unsubscribe
```

## Deploying to Production

### Option 1: Run on a VPS (Recommended)

```bash
# Use screen or tmux to keep it running
screen -S bot
python bot.py
# Press Ctrl+A, D to detach
```

### Option 2: Systemd Service (Linux)

Create `/etc/systemd/system/anglotec-bot.service`:

```ini
[Unit]
Description=AngloTec Study Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/telegram-bot
Environment=BOT_TOKEN=your_token
ExecStart=/path/to/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable anglotec-bot
sudo systemctl start anglotec-bot
sudo systemctl status anglotec-bot
```

### Option 3: Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV BOT_TOKEN=${BOT_TOKEN}
CMD ["python", "bot.py"]
```

```bash
docker build -t anglotec-bot .
docker run -e BOT_TOKEN=your_token -d anglotec-bot
```

## Updating the Bot

```bash
git pull  # If using git
# Or upload new files
pip install -r requirements.txt  # If dependencies changed
# Restart the bot
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "BOT_TOKEN not set" | Export the token or edit `config.py` |
| Bot doesn't respond | Check if token is valid at @BotFather |
| Auto-posts not working | Ensure system timezone is set to UTC |
| Import errors | Run `pip install -r requirements.txt` |
| Permission denied | Check file permissions with `chmod` |

## Traffic Generation Strategy

This bot is designed to drive organic traffic to your tools:

1. **Value-first approach** — Every interaction provides genuine study help
2. **Subtle footer** — Each message ends with a non-intrusive tool link
3. **Group infiltration** — Add to study groups where members discover the bot
4. **Shareable content** — Quizzes and vocabulary are highly shareable
5. **Daily engagement** — Subscribers get content daily, keeping your brand top-of-mind
6. **Word of mouth** — Quality content leads to organic recommendations

## License

This bot is built for AngloTec AI. Customize and deploy as needed.

## Support

For issues or questions, contact the development team.

---

Built with ❤️ by AngloTec AI | [tools.anglotec-ai.com](https://tools.anglotec-ai.com)
