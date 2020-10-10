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