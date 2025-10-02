import os
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Saintly Bot")
print(f"{ascii_banner}\b")

# Bot Token
os.environ["SAINTLY_BOT_TOKEN"] = input("Enter your bot token: ")
print("Saintly Bot Token:", os.environ["SAINTLY_BOT_TOKEN"])

print("Setup complete!")
