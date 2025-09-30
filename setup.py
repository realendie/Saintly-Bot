import os
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Saintly Bot")
print(f"{ascii_banner}\b")

# Bot Token
os.environ["SAINTLY_BOT_TOKEN"] = input("Enter your bot token: ")
print("Saintly Bot Token:", os.environ["SAINTLY_BOT_TOKEN"])

# Guild ID
os.environ["GUILD_ID"] = input("Enter your guild ID: ")
print("Guild ID:", os.environ["GUILD_ID"])

# Welcome Channel ID
os.environ["WELCOME_CHANNEL_ID"] = input("Enter your welcome channel ID: ")
print("Welcome Channel ID:", os.environ["WELCOME_CHANNEL_ID"])
os.environ["PENDING_ROLE_ID"] = input("Enter your pending role ID: ")
print("Pending Role ID:", os.environ["PENDING_ROLE_ID"])

# Mod Log Channel ID
os.environ["MOD_LOG_CHANNEL_ID"] = input("Enter your mod log channel ID: ")
print("Mod Log Channel ID:", os.environ["MOD_LOG_CHANNEL_ID"])
