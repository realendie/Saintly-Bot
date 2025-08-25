print("Starting Saintly City Roleplay Bot...")
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
intents.members = True
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
        mod_logs = interaction.guild.get_channel(MOD_LOGS_ID)
        if mod_logs:
            embed = discord.Embed(
                color=8496575,
                title="Kick Log",
            )
        embed.add_field(name="User", value=f"{user} (`{user.id}`)", inline=False)
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
                f"Failed to kick {user}. Error: {e}", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"Failed to kick {user}. Error: {e}", ephemeral=True
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
            f"**{user}** has been banned from the server."
        )

        # Ban Logging
        mod_logs = interaction.guild.get_channel(MOD_LOGS_ID)
        if mod_logs:
            embed = discord.Embed(
                color=8496575,
                title="Ban Log",
            )
        embed.add_field(name="User", value=f"{user} (`{user.id}`)", inline=False)
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
                f"Failed to Ban {user}. Error: {e}", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"Failed to Ban {user}. Error: {e}", ephemeral=True
            )


client.run(token)

# LICENSE

# Copyright 2025 Wyatt Johnson

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
