import discord
import json
import random

async def whosmells(message, bot):
    ''' Gets guild id and role id from json file.
    Creates a list of users in the desired role, picks a random user and sends message
    '''
    if message.content.lower().startswith("who smells?"):
            data = {}
            guild_id = str(message.guild.id)
            with open("roleid.json", "r") as file:
                contents = file.read()
                print(data)
                data = json.loads(contents)
                print(data)
            if guild_id in data:
                role_id = data[guild_id]
                print(role_id)
                guild = bot.get_guild(int(guild_id))
                roles = discord.utils.get(guild.roles, id=int(role_id))
                users = [m.name for m in roles.members]
                await message.channel.send(f"{random.choice(users)} smells!")
                return 0
            else:
                await message.channel.send("everyone smells!")
                return 0


async def roleid_set(message):
    '''Stores guild id and role id in json file'''
    if message.content.lower().startswith("!roleid"):
            try:
                with open("roleid.json", "r+") as file:
                    contents = file.read()
                    data = json.loads(contents)
                    guild_id = str(message.guild.id)
                    role_id = message.content.split(" ")[1].strip()
                    content = {guild_id:role_id}
                    data.update(content)
                    with open("roleid.json", "w") as file2:
                        json.dump(data, file2)
                        return 0
                    
            except FileNotFoundError:
                with open("roleid.json", "x") as file:
                    file.write("{}")
                    return 0