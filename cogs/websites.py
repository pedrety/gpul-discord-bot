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
        labs_emoji = discord.utils.get(self.bot.emojis, name='labs')
        await ctx.send(f'{labs_emoji} - https://labs.gpul.org/')
        school_emoji = discord.utils.get(self.bot.emojis, name='schools')
        await ctx.send(f'{school_emoji} - https://school.gpul.org/')
        coruna_hacks_emoji = discord.utils.get(self.bot.emojis, name='corunahacks')
        await ctx.send(f'{coruna_hacks_emoji} - https://corunahacks.gpul.org/')

    @commands.command()
    async def gpul(self, ctx):
        """Show GPUL website information"""
        gpul_emoji = discord.utils.get(self.bot.emojis, name='gpul')
        await ctx.send(f'{gpul_emoji} - https://gpul.org/')

    @commands.command()
    async def labs(self, ctx):
        """Show LABS website information"""
        labs_emoji = discord.utils.get(self.bot.emojis, name='labs')
        await ctx.send(f'{labs_emoji} - https://labs.gpul.org/')

    @commands.command()
    async def school(self, ctx):
        """Show SCHOOL website information"""
        school_emoji = discord.utils.get(self.bot.emojis, name='schools')
        await ctx.send(f'{school_emoji} - https://school.gpul.org/')

    @commands.command()
    async def hacks(self, ctx):
        """Show CORUÑA HACKS website information"""
        coruna_hacks_emoji = discord.utils.get(self.bot.emojis, name='corunahacks')
        await ctx.send(f'{coruna_hacks_emoji} - https://corunahacks.gpul.org/')

def setup(bot):
	bot.add_cog(Websites(bot))