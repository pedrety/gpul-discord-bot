import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print('Bot is ready!')

bot.load_extension(f'cogs.test')
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('TOKEN')