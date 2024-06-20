import discord
from discord.ext import commands

import os, re

class Replies(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message):
		if message.author == self.bot.user:
			return

		if message.content == "splendid":
			await message.reply("splendid")
			return

		if message.content == "you are my sunshine":
			await message.reply("my only sunshine")
			return

		if re.match('(?:.*)quoi(?:ent)?(?:\W*)$', message.content, flags=re.I):
			await message.reply('feur')
			
		# Replies only available to @Big Sister
		if discord.utils.get(message.author.roles, id=int(os.getenv('BIG_SISTER_ROLE_ID'))) != None:
			if message.content.startswith("bjr"):
				await message.reply('bjr grande soeur')
				

