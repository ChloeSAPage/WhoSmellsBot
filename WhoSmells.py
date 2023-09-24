import discord
import os
from dotenv import load_dotenv
import random
import json
import functions


load_dotenv()
TOKEN = os.getenv("WHOSMELLSTOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower().startswith("!"):
        await functions.roleid_set(message)
        
    await functions.whosmells(message, bot)

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Hey there! Please provide me with the role id of the " 
                            "stinkers. Start your message with '!roleid' followed by the ID.")
        break

bot.run(TOKEN)