import discord
from discord.ext import commands
import os

class AdminCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_role(int(os.getenv('BIG_SISTER_ROLE_ID')))
	async def showcommands(self, ctx: commands.Context):
		listofcommands = await self.bot.tree.fetch_commands(guild=discord.Object(id=int(os.getenv('TEST_SERV_ID'))))
		await ctx.reply(listofcommands)

	@commands.command()
	@commands.has_role(int(os.getenv('BIG_SISTER_ROLE_ID')))
	async def syncguildcommands(self, ctx: commands.Context):
		async with ctx.channel.typing():
			await self.bot.tree.sync(guild = discord.Object(id=int(os.getenv('TEST_SERV_ID'))))
		print(f'Synced slash commands for {self.bot.user}')
		await ctx.reply("Synced commands")

	@commands.command()
	@commands.has_role(int(os.getenv('BIG_SISTER_ROLE_ID')))
	async def evaluate(self, ctx: commands.Context, command_to_eval: str = "'no command has been passed'"):
		# await ctx.reply(command_to_eval)
		answer = eval(command_to_eval)
		await ctx.reply(f'```{answer}```')

	@commands.command()
	@commands.has_role(int(os.getenv('BIG_SISTER_ROLE_ID')))
	async def deleteglobalcommands(self, message: discord.Message):
		self.bot.tree.clear_commands(guild=None)
		await self.bot.tree.sync()
		await message.reply("Global commands deleted.")
