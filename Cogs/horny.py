import discord
from discord.ext import commands
import os, requests

class Horny(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.is_nsfw()
	async def horny(self, ctx: commands.Context, arg1: str = "", arg2: str = ""):
		apireq = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&limit=1&json=1&tags=sort:random"

		whichtoki = "+toki_(bunny)_(blue_archive)"
		rating = "+rating:explicit"

		if "safe" in [arg1, arg2]:
			rating = "+-rating:explicit"

		if "all" in [arg1, arg2]:
			whichtoki = "+toki_(blue_archive)"
			
		if "normal" in [arg1, arg2]:
			whichtoki = "+toki_(blue_archive)+-toki_(bunny)_(blue_archive)"
		
		apireq += whichtoki + rating

		response = requests.get(apireq)

		source_url = response.json()['post'][0].get('source')
		tags = response.json()['post'][0].get('tags')
		image = response.json()['post'][0].get('sample_url')

		if image == None:
			pass

		embed = discord.Embed(
			title="Toki H",
			url=source_url,
			description=tags,
			colour=discord.Colour.blue()
		)
		
		embed.set_image(url=image)

		embed.set_footer(
			text=image
		)

		await ctx.reply(embed=embed)