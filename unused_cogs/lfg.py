import discord
from discord.ext import commands

#PC ONLY RN

#will be using json files as storage for now
import json
import time

class lfg(commands.Cog):

    #structure: LTS/LFS/LFG/LFM
    #           Raid-Kürzel(Nur einen zulassen rn)
    #           (member count)
    #           Teilnehmer: Discord handle
    #                       Steam tag
    #           Timestamp {time.time()}
    s_groups = []



    def __init__(self, client):
        self.client = client

#        with open("./lfg/lfg.json","rw") as groups_handle:
#            self.s_groups = json.load(groups_handle)

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog lfg ready')
        return 0

def setup(client):
	client.add_cog(lfg(client))
