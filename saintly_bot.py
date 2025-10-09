print("Starting Saintly Bot...")
print("Loading libraries...")
import discord
from discord.ext import commands
from discord import app_commands
import os
import time

# Current time
current_time = time.gmtime()
formated_time = time.strftime(f"%m/%d/%y at %H:%M:%S")

# Discord Bot Token
print("Fetching Bot Token...")
token = str(os.getenv("SAINTLY_BOT_TOKEN"))

# Specific Guild ID required for command registration immediately after deployment
print("Fetching Discord Server ID...")
GUILD_ID = discord.Object(id=1408875149754765454)  # Discord Server ID
GUILD_NAME = "Your Discord Server"  # Discord Server Name
print("Fetching required channels...")
MOD_LOGS_ID = 1422732124750086160  # "mod-logs" Channel ID
WELCOMES_CHANNEL_ID = 1422732019019944068  # Welcomes Channel ID

print("Logging into Discord...")


class Client(commands.Bot):
    # Initializing bot and command prefixes
    async def on_ready(self):
        print(f"Logged in as {self.user}")

        # Attempting to sync commands to the Your Discord Server for immediate availability
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
intents.members = True
client = Client(
    command_prefix="!", intents=intents
)  # Command prefix, required to be there but not used

# Commands


# Setup Commands
@client.tree.command(
    name="set_mod_logs_channel",
    description="Use this command to set the channel in which you would like your mod logs to be sent.",
    guild=GUILD_ID,
)
async def modLogsChannel(interaction: discord.Interaction):
    id = str(interaction.channel_id)
    await interaction.response.send_message(
        "Mod Logs Channel set to this channel.", ephemeral=True
    )


# Ping/Pong Command
@client.tree.command(name="ping", description="Pong!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


# Current Time Command
@client.tree.command(
    name="time",
    description="Gives the user the current time and date in UTC",
    guild=GUILD_ID,
)
async def timeCommand(interaction: discord.Interaction):
    await interaction.response.send_message(f"It is currently **{formated_time}**")


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
    user_ID: int = user.id
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
            f"**<@{user_ID}>** has been kicked from the server."
        )

        # Kick Logging
        mod_logs = interaction.guild.get_channel(MOD_LOGS_ID)
        if mod_logs:
            embed = discord.Embed(
                color=8496575,
                title="Kick Log",
            )
        embed.add_field(name="User", value=f"<@{user_ID}>", inline=False)
        embed.add_field(
            name="Kicked by",
            value=f"{interaction.user} (`{interaction.user.id}`)",
            inline=False,
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Kicked on {formated_time}")

        await mod_logs.send(embed=embed)
    except Exception as e:
        # If we already had responded we must send message as follow up
        if interaction.response.is_done():
            await interaction.followup.send(
                f"Failed to kick **<@{user_ID}>**. Error: {e}", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"Failed to kick **<@{user_ID}>**. Error: {e}", ephemeral=True
            )


# Ban Command
@client.tree.command(
    name="ban",
    description="Bans a user from the server and logs it in #mod-logs",
    guild=GUILD_ID,
)
@app_commands.describe(user="User to ban", reason="Reason for baning")
async def kick(
    interaction: discord.Interaction,
    user: discord.Member,
    reason: str = "No reason provided",
):
    user_ID: int = user.id
    # Checking for ban permissions
    if not interaction.user.guild_permissions.ban_members:
        return await interaction.response.send_message(
            "You do not have permission to run this command.", ephemeral=True
        )

    # Stops user from banning higher or equal role members
    if user.top_role >= interaction.user.top_role:
        return await interaction.response.send_message(
            "You cannot ban this user.", ephemeral=True
        )
    # Stops user from banning themselves
    if user == interaction.user:
        return await interaction.response.send_message(
            "You cannot ban yourself.", ephemeral=True
        )

    # Banning Functionality
    try:
        await user.ban(reason=reason)
        await interaction.response.send_message(
            f"****<@{user_ID}>**** has been banned from the server."
        )

        # Ban Logging
        mod_logs = interaction.guild.get_channel(MOD_LOGS_ID)
        if mod_logs:
            embed = discord.Embed(
                color=8496575,
                title="Ban Log",
            )
        embed.add_field(
            name="User", value=f"**<@{user_ID}>** (`{user.id}`)", inline=False
        )
        embed.add_field(
            name="Banned by",
            value=f"{interaction.user} (`{interaction.user.id}`)",
            inline=False,
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Banned on {formated_time}")

        await mod_logs.send(embed=embed)
    except Exception as e:
        # If we already had responded we must send message as follow up
        if interaction.response.is_done():
            await interaction.followup.send(
                f"Failed to Ban **<@{user_ID}>**. Error: {e}", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"Failed to Ban **<@{user_ID}>**. Error: {e}", ephemeral=True
            )


# Welcome Messages


@client.event
async def on_member_join(member: discord.Member):
    welcomes_channel = member.guild.get_channel(WELCOMES_CHANNEL_ID)
    if welcomes_channel:
        embed = discord.Embed(
            color=8496575,
            title=f"Welcome to {GUILD_NAME}!",
            description=f"Hello {member.mention} and welcome to {GUILD_NAME}! Make sure to read the rules in <#1367291515977596948> and head to <#1389789262504788019> to get verified. Enjoy your stay!",
        )
        # embed.set_image(
        # url="an image to display at the bottom of the embed"
        # )

        await welcomes_channel.send(embed=embed)
    # Pending Residency Role
    role = member.guild.get_role(1422732060782755941)  # Pending Residency Role ID
    if role:
        await member.add_roles(role, reason="Automatic Pending Residency Role")


# Reaction Roles

REACTION_ROLES = {
    "✅": 1381509714835148840,  # Emoji: Role ID
}

MESSAGE_ID = 1409426311717326849  # The message ID where reactions should count


@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.message_id != MESSAGE_ID:
        return

    guild = client.get_guild(payload.guild_id)
    if guild is None:
        return

    role_id = REACTION_ROLES.get(str(payload.emoji))
    if role_id is None:
        return

    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None or member.bot:
        return

    await member.add_roles(role, reason="Reaction role added")
    print(f"✅ Added {role.name} to {member.display_name}")


@client.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.message_id != MESSAGE_ID:
        return

    guild = client.get_guild(payload.guild_id)
    if guild is None:
        return

    role_id = REACTION_ROLES.get(str(payload.emoji))
    if role_id is None:
        return

    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    await member.remove_roles(role, reason="Reaction role removed")
    print(f"❌ Removed {role.name} from {member.display_name}")


client.run(token)

# LICENSE

# Copyright 2025 Wyatt Johnson

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
