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

class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def social(self, ctx):
        """Show all social media information"""
        twitter_emoji = discord.utils.get(self.bot.emojis, name='twitter')
        await ctx.send(f'{twitter_emoji} - https://twitter.com/gpul_')
        meetup_emoji = discord.utils.get(self.bot.emojis, name='meetup')
        await ctx.send(f'{meetup_emoji} - https://www.meetup.com/es-ES/GPUL-Labs/')
        facebook_emoji = discord.utils.get(self.bot.emojis, name='facebook')
        await ctx.send(f'{facebook_emoji} - https://www.facebook.com/gpulfic/')

    @commands.command()
    async def twitter(self, ctx):
        """Show twitter social media information"""
        twitter_emoji = discord.utils.get(self.bot.emojis, name='twitter')
        await ctx.send(f'{twitter_emoji} - https://twitter.com/gpul_')

    @commands.command()
    async def meetup(self, ctx):
        """Show meetup social media information"""
        meetup_emoji = discord.utils.get(self.bot.emojis, name='meetup')
        await ctx.send(f'{meetup_emoji} - https://www.meetup.com/es-ES/GPUL-Labs/')

    @commands.command()
    async def facebook(self, ctx):
        """Show facebook social media information"""
        facebook_emoji = discord.utils.get(self.bot.emojis, name='facebook')
        await ctx.send(f'{facebook_emoji} - https://www.facebook.com/gpulfic/')

def setup(bot):
	bot.add_cog(Social(bot))