print("Starting Saintly City Roleplay Bot...")
print("Loading libraries...")
import discord
from discord.ext import commands
from discord import app_commands
import os

# Discord Bot Token
print("Fetching Bot Token...")
token = os.getenv("SAINTLY_BOT_TOKEN")

# Specific Guild ID required for command registration immediately after deployment
print("Fetching Saintly City Discord Server ID...")
GUILD_ID = discord.Object(id=1366991874019168256)  # Saintly City Discord Server ID

print("Logging into Discord...")


class Client(commands.Bot):
    # Initializing bot and command prefixes
    async def on_ready(self):
        print(f"Logged in as {self.user}")

        # Attempting to synce commands to the Saintly City Roleplay Server for immediate availability
        print("Syncing commands to the guild...")
        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f"Synced {len(synced)} commands to the guild.")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return


# Bot intents
print("Loading bot intents...")
intents = discord.Intents.default()
intents.message_content = True
client = Client(
    command_prefix="!", intents=intents
)  # Command prefix, required to be there but not used

# Commands


# Ping/Pong Command
@client.tree.command(name="ping", description="Pong!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


# f8 Command
@client.tree.command(
    name="f8",
    description="Gives the user the server's f8 join command.",
    guild=GUILD_ID,
)
async def f8(interaction: discord.Interaction):
    await interaction.response.send_message(
        "To join the server via the f8 menu press f8 then paste this command:\n```cfx.re/join/o7edmx```"
    )


client.run(token)
