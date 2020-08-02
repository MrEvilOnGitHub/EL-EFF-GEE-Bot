import discord
from discord import User
from discord.ext import commands
import sqlite3
import useful_functions
import descriptions

class uid_test(commands.Cog):

    conn = sqlite3.connect("uids.db")
    cursor = conn.cursor()
    #table: ids (steam, discord)

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog uid-test ready")
        return 0

    @commands.command(description=descriptions.d_uid_test.print_uid, hidden=True)
    async def print_uid(self, ctx):
        """print the discord-id of the invoker"""
        print(ctx.author.id)
        await ctx.send(f"uid: {ctx.author.id}")
        return 0

    @commands.command(description=descriptions.d_uid_test.add_steam)
    async def add_steam(self, ctx, sid = None):
        """add the invoker\'s steam id to the database"""
        if sid is not None:
            try:
                sid = int(sid)
                did = int(ctx.author.id)
            except :
                await ctx.send("Your steam id is a number, not a word. Duh")
                return 1
            self.cursor.execute(f"SELECT * FROM ids WHERE discord = {did}")
            data=self.cursor.fetchone()
            if data is None:
                try:
                    self.conn.execute("INSERT into ids values(?, ?)", (sid, did))
                    self.conn.commit()
                    await ctx.send("Your steam-id has been commited to the list")
                except Exception as e:
                    await ctx.send("something went wrong, try again later")
                    print(e)
                    return 1
            else:
                await ctx.send("There\'s already a linked steam id to your discord profile")
        else:
            await ctx.send("You need to supply a steam-id to add one")

    @commands.command(description=descriptions.d_uid_test.remove_steam)
    async def remove_steam(self, ctx):
        did = int(ctx.author.id)
        self.cursor.execute("SELECT * FROM ids WHERE discord = ?", (did, ))
        data = self.cursor.fetchone()
        if data is not None:
            self.conn.execute("DELETE FROM ids WHERE discord = ?", (did, ))
            self.conn.commit()
            await ctx.send("Your steam-id has been removed")
            return 0
        else:
            await ctx.send("There is no linked steam-id")
            return 0

    @commands.command(description=descriptions.d_uid_test.steam_id)
    async def steam_id(self, ctx, user: User = None):
        if user is None:
            did = int(ctx.author.id)
            self.cursor.execute("SELECT * FROM ids WHERE discord = ?", (did, ))
            data = self.cursor.fetchone()
            if data is not None:
                await ctx.send(f"Your registered steam-id is: {data[0]}")
                return 0
            else:
                await ctx.send("There is no registered steam-id for your account")
        else:
            try:
                did = int(user.id)
            except Exception as e:
                print(e)
                await ctx.send("You must mention (@) the user whose steam-id you want to know")
                return 0
            self.cursor.execute("SELECT steam FROM ids WHERE discord = ?", (did, ))
            sid = self.cursor.fetchone()
            if sid is not None:
                await ctx.send(f"{user.mention()}'s steam-id is {sid[0]}")
                return 0
            else:
                await ctx.send(f"{user.mention()} has no registered steam-id")
                return 0

def setup(client):
    client.add_cog(uid_test(client))
