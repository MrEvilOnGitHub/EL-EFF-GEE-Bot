import discord
from discord.ext import commands
import descriptions

class example(commands.Cog):
	def __init__(self, client):
		self.client = client

	#events
	@commands.Cog.listener()
	async def on_ready():
		print('Cog Example ready')

	#Commands
	@commands.command(description=descriptions.d_example.ping1)
	async def ping1(self, ctx):
		await ctx.send('Pong')

def setup(client):
	client.add_cog(example(client))
