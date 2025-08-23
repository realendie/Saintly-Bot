print("Starting Saintly Bot...")

print("Loading libraries...")
import discord
from discord import app_commands
import os
import time

# Accesing bot token from environment variable
print("Fetching bot token...")
token = os.getenv("SAINTLY_BOT_TOKEN")

# Bot discord intents
print("Setting Intents")
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)

# Command tree
print("Setting up command tree...")
tree = app_commands.CommandTree(client)


print("Connecting to Discord...")


@client.event
async def on_ready():
    currenttime = time.localtime()
    format_time = time.strftime("%H:%M:%S", currenttime)

    print(f"Bot logged in as {client.user}")
    print(f"Bot online as of {format_time}!")


client.run(token)
