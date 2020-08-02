import discord
from discord.ext import commands
import useful_functions
import descriptions

class list_manipulation(commands.Cog):

    tlist = [(1, "name1") , (2, "name2") , (3, "name3")]

    def __init__(self, client):
        self.client = client

#events

    @commands.Cog.listener()
    async def on_ready():
        print('Cog list_manipulation ready')
        return 0

#Commands

    @commands.command(description=descriptions.d_list_manipulation.echo)
    async def echo(self, ctx, *, message):
        await ctx.send(f"{message}")

    #add value name as identifierto tlist
    @commands.command(description=descriptions.d_list_manipulation.al)
    async def al(self, ctx, identifier, name):
        try:
            identifier = int(identifier)
            if identifier >= 1:
                i = (identifier, name)
                self.tlist.append(i)
            else:
                await ctx.send("identifier must be greater than 0")
        except ValueError:
            await ctx.send("Please enter a number as identifier")
        return 0

    #print every entry in tlist
    @commands.command(description=descriptions.d_list_manipulation.pl)
    async def pl(self, ctx):
        for tuples in self.tlist:
            print(tuples)
            print(type(tuples))
            await ctx.send(f"{tuples}")
        return 0

# Does work properly, but uses a static list for now
    @commands.command(description=descriptions.d_list_manipulation.getident)
    async def getident(self, ctx, name):
        try:
            index = useful_functions.find_in_list_of_list(self.tlist, name)
            print(index)
            await ctx.send(f"{str(self.tlist[index[0]][0])}")
        except ValueError:
            await ctx.send(f"{name} is not in the list")
        return 0

def setup(client):
	client.add_cog(list_manipulation(client))

# create sqlite table: create table "name" ("name type")
# add values: insert into "table" values (values sorted by columns)
# select certain values from list: select "column" from "table" where "filter"
# connect to db: connection = sqlite3.connect("filename")
# create cursor: cursor = connection.cursor()
# execute sql commands: cursor.execute("command")
# commit changes: cursor.commit()
