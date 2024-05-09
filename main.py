import discord
from discord.ext import commands
from discord import app_commands

import logging
import random, os, re, requests

from secret import *

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.members = True

bot = commands.Bot(command_prefix="^", intents=intents)

# Startup
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Say hello to new people
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"Pyon pyon {member.mention} ✌️🐇️✌️")

# Replying to messages
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    if message.content == "splendid":
        await message.reply("splendid")
        return

    if message.content == "you are my sunshine":
        await message.reply("my only sunshine")
        return


    # Replies only available to @Big Sister
    if discord.utils.get(message.author.roles, id=BIG_SISTER_ROLE_ID) != None:
        if message.content.startswith("bjr"):
            await message.reply('bjr grande soeur')
            
    if re.match('(?:.*)quoi(?:ent)?(?:\W*)$', message.content, flags=re.I):
        await message.reply('feur')

    await bot.process_commands(message)

# Slash Commands

# Ping
@bot.tree.command(
    name='ping',
    description='Pong !'
)
@app_commands.guilds(discord.Object(id=TEST_SERV_ID))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong !")

# Roll a dice
@bot.tree.command(
    name='rolladice',
    description='Roll a n-sided die.'
)
@app_commands.guilds(discord.Object(id=TEST_SERV_ID))
async def rolladice(interaction: discord.Interaction, sides:int = 6):
    rolled = random.randint(1, sides)
    await interaction.response.send_message(f"🎲 You rolled a {rolled} on a {sides}-sided die")

# Regular Commands

@bot.command()
@commands.is_nsfw()
async def horny(ctx: commands.Context, arg1: str = "", arg2: str = ""):
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

# Admin Commands
  
@bot.command()
@commands.has_role(BIG_SISTER_ROLE_ID)
async def showcommands(ctx: commands.Context):
    await message.reply(bot.tree.fetch_commands(guild=discord.Object(id=TEST_SERV_ID)))

@bot.command()
@commands.has_role(BIG_SISTER_ROLE_ID)
async def syncguildcommands(ctx: commands.Context):
    async with message.channel.typing():
        await bot.tree.sync(guild = discord.Object(id=TEST_SERV_ID))
    print(f'Synced slash commands for {bot.user}')
    await message.reply("Synced commands")

@bot.command()
@commands.has_role(BIG_SISTER_ROLE_ID)
async def evaluate(ctx: commands.Context, command_to_eval: str = "'no command has been passed'"):
    answer = eval(command_to_eval)
    await ctx.reply(f'```{answer}```')

@bot.command()
@commands.has_role(BIG_SISTER_ROLE_ID)
async def deleteglobalcommands(message: discord.Message):
    bot.tree.clear_commands(guild=None)
    await bot.tree.sync()
    await message.reply("Global commands deleted.")

### Error handeling

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRole):
        await ctx.message.reply("You do not have the correct role.")
    else:
        await ctx.message.reply(error)

# Awaken Toki
bot.run(token=BOT_TOKEN, log_handler=handler, log_level=logging.INFO,)
