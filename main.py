import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('Bot is ready!')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)