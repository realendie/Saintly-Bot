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
print("Fetching mod logs channel...")
MOD_LOGS_ID = 1409267262812197015  # "mod-logs" Chanel ID

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


# Moderation Tools


# Kick Command
@client.tree.command(
    name="kick",
    description="Kicks a user from the server and logs it in #mod-logs",
    guild=GUILD_ID,
)
@app_commands.describe(user="User to kick", reason="Reason for kicking")
async def kick(
    interaction: discord.Interaction,
    user: discord.Member,
    reason: str = "No reason provided",
):
    # Checking for kick permissions
    if not interaction.user.guild_permissions.kick_members:
        return await interaction.response.send_message(
            "You do not have permission to run this command.", ephemeral=True
        )

    # Stops user from kicking higher or equal role members
    if user.top_role >= interaction.user.top_role:
        return await interaction.response.send_message(
            "You cannot kick this user.", ephemeral=True
        )
    # Stops user from kicking themselves
    if user == interaction.user:
        return await interaction.response.send_message(
            "You cannot kick yourself.", ephemeral=True
        )

    # Kicking Functionality
    try:
        await user.kick(reason=reason)
        await interaction.response.send_message(
            f"**{user}** has been kicked from the server."
        )

        # Kick Logging
        if 

    except Exception as e:
        return await interaction.response.send_message(
            f"Failed to kick {user}. Error: {e}", ephemeral=True
        )


client.run(token)
