'''
  gpul-discord-bot: GPUL discord bot implemented with python.
	
	This file is part of gpul-discord-bot.

  gpul-discord-bot is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  gpul-discord-bot is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with gpul-discord-bot.  If not, see <https://www.gnu.org/licenses/>.
'''

from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def ping(self, ctx):
		"""Says Pong"""
		await ctx.send("Pong")

def setup(bot):
	bot.add_cog(Test(bot))