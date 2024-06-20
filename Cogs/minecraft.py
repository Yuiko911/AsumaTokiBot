import discord
from discord.ext import commands
import os

def is_in_mc_channel(ctx: commands.Context):
	return ctx.channel.id == int(os.getenv('MINECRAFT_CHANNEL_ID'))

class Minecraft(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_role(int(os.getenv('GDD_ROLE_ID')))
	@commands.check(is_in_mc_channel)
	async def mcstatus(self, ctx: commands.Context):
		await ctx.reply("status of the mc server (running, nb of ppl)")

	@commands.command()
	@commands.has_role(int(os.getenv('GDD_ROLE_ID')))
	@commands.check(is_in_mc_channel)
	async def mcstart(self, ctx: commands.Context):
		await ctx.reply("starting")

	@commands.command()
	@commands.has_role(int(os.getenv('GDD_ROLE_ID')))
	@commands.check(is_in_mc_channel)
	async def mcstop(self, ctx: commands.Context):
		await ctx.reply("stopping")

	@commands.command()
	@commands.has_role(int(os.getenv('GDD_ROLE_ID')))
	@commands.check(is_in_mc_channel)
	async def mcshowlogs(self, ctx: commands.Context):
		await ctx.reply("logslogslogs")
