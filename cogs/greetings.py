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

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(761965902568488986)
        if channel is not None:
            await channel.send('Bienvenido al servidor de GPUL {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hola {}'.format(member.mention))
        else:
            await ctx.send('Hola {}... Esto me resulta familiar.'.format(member.mention))
        self._last_member = member

def setup(bot):
	bot.add_cog(Greetings(bot))