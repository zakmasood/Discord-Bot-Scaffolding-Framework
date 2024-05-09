import discord
from discord.ext import commands, tasks
# Misc
import os
from dotenv import load_dotenv
# DB and Networking
import requests
import asyncio
import sqlite3
# Date / Time
from datetime import datetime, timedelta
from dateutil import parser
import time
# Middle DB access layer
import dbAccessLayer
from dbAccessLayer import createModeration

#----------------------------------------------------------------


# Connect to the SQLite database

load_dotenv()

token = os.getenv('DiscordToken')
loggingChannelID = os.getenv('LoggingChannelID')
muteRoleID = os.getenv('MuteRoleID')

conn = sqlite3.connect('./myModerationDatabase.db')
c = conn.cursor()

def handleNewUser(UserID, Username, Avatar, IsBot):
    startTime = time.time()
    c.execute("SELECT * FROM User WHERE UserID = ?", (UserID,))
    user = c.fetchone()
    
    if not user:
        c.execute("INSERT INTO User (UserID, Username, Avatar, IsBot) VALUES (?, ?, ?, ?)",
                    (UserID, Username, Avatar, IsBot))
        conn.commit()
        
    endTime = time.time()
    writeTime = endTime - startTime
    print(f"Total WRITE time for user {UserID}: {writeTime} seconds")

# Set the bot's command prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#--------------------------------[Events]--------------------------------

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is up and running!')

@bot.event
async def on_message(message):
    # Return if the message author is self
    if message.author.bot:
        return
    
    userID = message.author.id
    username = message.author.name
    avatar = str(message.author.avatar.url)
    isBot = message.author.bot
    
    handleNewUser(userID, username, avatar, isBot)
    
    # Increment total messages count for the user
    try:
        c.execute("UPDATE User SET TotalMessages = TotalMessages + 1 WHERE UserID = ?", (userID,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating total messages count: {e}")

    await bot.process_commands(message)
    
@bot.event
async def on_reaction_add(reaction, user):
    # Return if the reaction is added by a bot
    if user.bot:
        return

    userID = user.id

    # Increment total reactions count for the user
    try:
        c.execute("UPDATE User SET TotalReactions = TotalReactions + 1 WHERE UserID = ?", (userID,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating total reactions count: {e}")
    
#--------------------------------[Commands]------------------------------

@bot.command()
@commands.has_permissions(kick_members=True)
async def moderate(ctx, action: str, member: discord.Member, *, reason=None):
    """Moderate a user in the server"""
    validActions = ["warn", "mute", "kick", "ban", "unmute"]
    action = action.lower()

    if action not in validActions:
        await ctx.send(f"Invalid action '{action}'. Valid actions are: {', '.join(validActions)}")
        return

    if member is None or member == ctx.author:
        await ctx.send(f"You cannot {action} yourself!")
        return

    serverID = ctx.guild.id
    userID = member.id
    moderatorID = ctx.author.id
    actionUpper = action.upper()
    createdAt = datetime.utcnow()

    if reason is None:
        reason = "No reason provided."

    embed = discord.Embed(
        title=f"User {actionUpper}ed",
        description=f"You have been {action}ed by {ctx.author.mention} from {ctx.guild.name}",
        color=discord.Color.red()
    )
    embed.add_field(name="Reason", value=reason)

    createModeration(serverID, str(userID), actionUpper, reason, moderatorID, createdAt)

    logChannel = bot.get_channel(loggingChannelID)
    if logChannel:
        logEmbed = discord.Embed(
            title=f"User {actionUpper}ed",
            description=f"{member.mention} has been {action}ed by {ctx.author.mention}",
            color=discord.Color.red()
        )
        logEmbed.add_field(name="Reason", value=reason)
        await logChannel.send(embed=logEmbed)

    await member.send(embed=embed)

    if action == "mute":
        muteRole = discord.utils.get(ctx.guild.roles, name="Muted")
        if muteRole:
            await member.add_roles(muteRole)
        else:
            await ctx.send("Could not find the 'Muted' role.")
    elif action == "kick":
        await member.kick(reason=reason)
    elif action == "ban":
        await member.ban(reason=reason)
    elif action == "unmute":
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role:
            await member.remove_roles(muteRole)
        else:
            await ctx.send("Could not find the 'Muted' role.")
        
# Run the bot with your bot token
bot.run(token)