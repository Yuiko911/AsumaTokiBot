import discord
from discord.ext import commands

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member: discord.Member):
	    guild = member.guild
	    if guild.system_channel is not None:
	        await guild.system_channel.send(f"Pyon pyon {member.mention} ✌️🐇️✌️")
