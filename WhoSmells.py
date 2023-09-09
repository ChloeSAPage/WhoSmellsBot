import discord
import os
from dotenv import load_dotenv
import random


load_dotenv()
TOKEN = os.getenv("WHOSMELLSTOKEN")
serverid_cummies = int(os.getenv("serverid_cummies"))
IRL_ROLE_ID = int(os.getenv("IRL_ROLE_ID"))
print(IRL_ROLE_ID, serverid_cummies)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    guild = client.get_guild(serverid_cummies)
    roles = discord.utils.get(guild.roles, id=IRL_ROLE_ID)
    global users
    users = [m.name for m in roles.members]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('who smells?'):
        await message.channel.send(f"{random.choice(users)} smells!")

client.run(TOKEN)