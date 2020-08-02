#@client.command()
#async def kick(ctx, member : discord.member, *, reason=None):
#	await member.kick(reason = reason)
#	await ctx.channel.purge(limit = 1)
#	await ctx.send(f'{member.displayname} has been kicked \nReason: {reason}')

#@client.command()
#async def ban(ctx, member : discord.member, *, reason=None):
#	await member.ban(reason = reason)
#	await ctx.channel.purge(limit = 1)
#	await ctx.send(f'{member.displayname} has been banned \nReason: {reason}')

#@client.command()
#async def unban(ctx, *, member):
#	banned_users = await ctx.guild.bans()
#	member_name, member_number = member.split('#')
#	for ban_entry in banned_users:
#		user = ban_entry.user
#		if(user.name == member_name and user.discriminator == member_number):
#			await ctx.guild.unban(user)
#			await ctx.send(f'{user.mention} has been unbanned')

#@client.command(aliases=['8ball'])
#async def _8ball(ctx, *, question):
#	responses = ["1","2","3","4"]
#	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#@client.event
#async def on_member_join(member):
#	print(f'{member} has joined the server')

#@client.event
#async def on_member_remove(member):
#	print(f'{member} has left the server')