# Saintly Bot

A self hosted, code centered, generic discord bot for your server. Saintly Bot is made as a solution to expensive and propritary discord bots that make you pay for basic features.

## Modules

Saintly Bot has some basic modules that every sever would need. Some include:

- Moderation Commands (kick/ban/logging)
- Welcome messages

## Installation

There are two simple ways to host Saintly Bot for your self.

## Requirements

- Python >= 3.13
- Requirements listed in `requirments.txt`
- A Discord account

### Discord Developer Setup

Follow the steps listed here to setup your discord bot: [Create a Discord Bot and Add Permissions](https://scribehow.com/viewer/Create_a_Discord_Bot_and_Add_Permissions__Rzi4bF2KQeuBAyT2ZDtlbA?add_to_team_with_invite=True&sharer_domain=gmail.com&sharer_id=3239cd2c-7eb1-472f-a240-3cfebebe77bf)

### Local Hosting

To host Saintly Bot locally via your terminal follow these steps:

1. Clone the repository: `git clone https://github.com/realendie/Saintly-Bot.git`
2. CD into the directory: `cd Saintly-Bot/`
3. Install requirements:
3.1 Create virtual environment: `python3 -m venv .venv`
3.2 Activate virtual environment: `source .venv/bin/activate`
3.3 Upgrade PIP: `pip install --upgrade pip`
3.4 Install Python packages: `pip install -r ./requirements.txt`
4. Fill in your servers information in `saintly_bot.py`
5. Set your bot token to an evironment variable named `SAINTLY_BOT_TOKEN` (Method depends on your OS)
6. Run the bot: `python3 saintly_bot.py`

### Docker Hosting

1. Clone the repository: `git clone https://github.com/realendie/Saintly-Bot.git`
2. CD into the directory: `cd Saintly-Bot/`
3. Make a new file named `.env`, inside it put:

```env
SAINTLY_BOT_TOKEN = "your_bot_token"
```

4. Start the docker container `docker-compose up -d`
