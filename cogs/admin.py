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


class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    guild = self.bot.get_guild(payload.guild_id)
    member_role = discord.utils.get(guild.roles, name="Miembro")
    member = guild.get_member(payload.user_id)

    if str(payload.channel_id) in '761965902568488982':
      if str(payload.emoji) == "👌":
        await member.add_roles(member_role, atomic = True)


def setup(bot):
	bot.add_cog(Admin(bot))