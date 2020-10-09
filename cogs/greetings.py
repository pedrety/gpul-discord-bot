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