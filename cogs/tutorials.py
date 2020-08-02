import discord
from discord.ext import commands
import descriptions

class tutorials(commands.Cog):
    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog tutorials ready')
        return 0

    #Commands
    @commands.command(description=descriptions.d_tutorials.ping)
    async def ping(self, ctx):
        print("command ping received")
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')
        """
        Returns ping in ms
        """
        return 0

    @commands.command(description=descriptions.d_tutorials.clear, hidden=True)
    async def clear(self, ctx, amount = 5):
        print("command clear received")
        if(amount > 0):
            await ctx.channel.purge(limit = amount)
        else:
            await ctx.send('Clear amount must be greater than 0')
        """
        Clears the current channel from x amount of messages
        When no value is specified, clear it by 5
        """
        return 0

def setup(client):
	client.add_cog(tutorials(client))
