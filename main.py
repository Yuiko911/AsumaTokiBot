import os

from dotenv import load_dotenv
load_dotenv(".env")

import discord
from discord.ext import commands
from discord import app_commands

from Cogs.greetings import Greetings
from Cogs.admin import AdminCommands
from Cogs.replies import Replies
from Cogs.minecraft import Minecraft
from Cogs.horny import Horny

class Bot(commands.Bot):
	def __init__(self):
		prefix = "^"

		intents = discord.Intents.default()
		intents.message_content = True
		# intents.dm_messages = True
		intents.members = True

		super().__init__(
			command_prefix=prefix, 
			intents=intents
		)

	async def setup_hook(self):
		await self.add_cog(Minecraft(self))
		await self.add_cog(Greetings(self))
		await self.add_cog(AdminCommands(self))
		await self.add_cog(Replies(self))
		await self.add_cog(Horny(self))

	async def on_ready(self):
		print(f'We have logged in as {bot.user}')


bot = Bot()
bot.run(token=os.getenv("BOT_TOKEN"))
