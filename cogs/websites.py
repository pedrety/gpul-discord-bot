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

import discord
from discord.ext import commands

class Websites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def websites(self, ctx):
        """Show all websites information"""
        gpul_emoji = discord.utils.get(self.bot.emojis, name='gpul')
        await ctx.send(f'{gpul_emoji} - https://gpul.org/')
        await ctx.send(f':gpul_labs: - https://labs.gpul.org/')
        await ctx.send(f':gpul_school: - https://school.gpul.org/')
        await ctx.send(f':gpul_coruna_hacks: - https://corunahacks.gpul.org/')

    @commands.command()
    async def gpul(self, ctx):
        """Show GPUL website information"""
        gpul_emoji = discord.utils.get(self.bot.emojis, name='gpul')
        await ctx.send(f'{gpul_emoji} - https://gpul.org/')

    @commands.command()
    async def labs(self, ctx):
        """Show LABS website information"""
        await ctx.send(f':gpul_labs: - https://labs.gpul.org/')

    @commands.command()
    async def school(self, ctx):
        """Show SCHOOL website information"""
        await ctx.send(f':gpul_school: - https://school.gpul.org/')

    @commands.command()
    async def hacks(self, ctx):
        """Show CORUÑA HACKS website information"""
        await ctx.send(f':gpul_coruna_hacks: - https://corunahacks.gpul.org/')

def setup(bot):
	bot.add_cog(Websites(bot))