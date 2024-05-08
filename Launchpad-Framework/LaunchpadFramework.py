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

#----------------------------------------------------------------

# Connect to the SQLite database
conn = sqlite3.connect('./Launchpad.db')
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

#--------------------------------[Events!]--------------------------------

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is up and running!')

@bot.event
async def on_message(message):
    # Return if the message author is self
    if message.author.bot:
        return
    
    UserID = message.author.id
    Username = message.author.name
    Avatar = str(message.author.avatar.url)
    IsBot = message.author.bot
    
    handleNewUser(UserID, Username, Avatar, IsBot)

# Run the bot with your bot token
load_dotenv()
token = os.getenv('DiscordToken')
bot.run(token)