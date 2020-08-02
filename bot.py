import sys
try:
	import discord
	from discord.ext import commands
	import os
	import json
	import descriptions
	import bisect
except:
	print("the modules discord, os & json must be installed for this bot to work")
	sys.exit(1)

#discord bot authenticator laden
with open("auth.json", "r") as auth_file:
	auth_raw = json.load(auth_file)

#load disabled channels list
#might break the bot currently
#with open("ignored_channels.json", "r+") as ic_handler:
#	ignored_channels = json.load(ic_handler)
#ignored_set = set(ignored_channels)


client = commands.Bot(command_prefix = '§')

@client.event
async def on_ready():
	print('Bot is ready')

#@client.event
#async def on_message(message):
#	print("message received")
#	print(message.content)
	#ignore messages from the bot
	#if message.author == client.User:
	#	return
	#ignore messages in list
#	if message.channel.id in ignored_set:
#		return

#erweiterung laden
@client.command(description=descriptions.d_bot.load)
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

#erweiterung entladen
@client.command(description=descriptions.d_bot.unload)
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

@client.command()
async def block_channel(ctx):
	ignored_channels.append(ctx.channel.id)
	json.dump(ignored_channels, ic_handler)
	ignored_set = set(ignored_channels)



#alle erweiterungen bei start laden
for filename in os.listdir('./cogs'):
			if filename.endswith('.py'):
				client.load_extension(f'cogs.{filename[:-3]}')

client.run(auth_raw["token"])
