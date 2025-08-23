import discord
from discord.ext import commands
from discord import app_commands
import os

token = os.getenv("SAINTLY_BOT_TOKEN")


class Client(commands.Bot):
    async def on_ready(self):
        print(f"We have logged in as {self.user}")

        try:
            guild = discord.Object(id=1366991874019168256)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to the guild {guild}.")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello {message.author.mention}!")


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1366991874019168256)  # Saintly City Discord Server ID


@client.tree.command(name="hello", description="Say hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello there! test")


client.run(token)
