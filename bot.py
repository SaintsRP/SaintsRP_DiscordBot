import discord
from discord.ext import commands
import config
import os
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("COGS LOADED")
        print("------------------------------------------")
        print(filename[:-3])
        print('------------------------------------------')

bot.run(config.TOKEN)