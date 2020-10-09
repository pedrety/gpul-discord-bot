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