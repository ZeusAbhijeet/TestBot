import discord
import asyncio
from discord.ext import commands

class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command(name='clear', aliases=['purge', 'delete'], help='Clears the given amount of messages. Clears 3 messages by default.')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=3):
		deleted = await ctx.channel.purge(limit=amount+1)
		msg = await ctx.send(f'Deleted {len(deleted)} messages')
		await asyncio.sleep(5)
		await msg.delete()
	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Manage Messages Permission to run this command.')

	@commands.command(name='kick')
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, *, reason='None'):
		await member.kick(reason=reason)
		await ctx.send(f'Kicked {member.mention}\nReason: {reason}')
	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Kick Members Permission to run this command.')

	@commands.command(name='ban')
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member, *, reason='None'):
		await member.ban(reason=reason)
		await ctx.send(f'Banned {member.mention}\nReason: {reason}')
	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Ban Members Permission to run this command.')

	@commands.Cog.listener()
	async def on_ready(self):
		print('Cog: Moderation is Online')

def setup(client):
	client.add_cog(Moderation(client))
