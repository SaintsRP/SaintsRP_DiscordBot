import discord
from discord.ext import commands
import config
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


bot.run(config.TOKEN)