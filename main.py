import discord
from discord.ext import commands, tasks
import os
import random

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = "-", case_insensitive = True, intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
      print('Bot ligado com Sucesso {0.user}'.format(client))
      test.start() 

@tasks.loop(minutes = 1)
async def test():
  status = [
            "a {} servers | -help".format(len (client.guilds)), 
            'a propagandas...',
            "a {} usúarios | -help".format(len (client.users)),
            'a Batatinha 1 2 3'
            ]
  numero = random.choice(status)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=numero))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODkxMjUzNzU2ODYyMjcxNTEw.YU7qvg.Y4LSBPY36qy3GnG_oK0mwgwtuWo')