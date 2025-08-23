import discord
from discord.ext import commands
import os
import time

# Accesing bot token from environment variable

token = os.getenv("SAINTLY_BOT_TOKEN")

# Initailize Bot

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)


@client.event
async def on_ready():

    currenttime = time.localtime()
    format_time = time.strftime("%H:%M:%S", currenttime)

    print(f"Bot logged in as{client.user}")
    print(f"Bot online as of {format_time}!")


# $hello Command


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello! Welcome to Saintly City Roleplay!")

# Admin Commands

#@bot.command(name="shutdown")
#async def






client.run(token)