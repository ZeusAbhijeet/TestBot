import discord
import os
import random
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready.')
	print(f'Logged in as: {client.user.name} ID: {client.user.id}')
	print(f'Online in guilds:')
	for server in client.guilds:
		print(f'Guild name: {server.name}')
		print(f'Guild ID: {server.id}')

if __name__ == '__main__':
	extensions = ['Utility', 'Fun', 'Moderation']# 'Fun', 'Moderation'
	for extension in extensions:
		client.load_extension(extension)

@client.command(name='load')
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
	client.load_extension(extension)
	await ctx.send(f'Loaded Extension: {extension}')

@client.command(name='unload')
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
	client.unload_extension(extension)
	await ctx.send(f'Unloaded Extension: {extension}')

@client.command(name='reload')
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
	client.unload_extension(extension)
	client.load_extension(extension)
	await ctx.send(f'Reloaded Extention: {extension}')

#for filename in os.listdir('./cogs'):
#	if filename.endswith('.py'):
#		client.load_extension(f'cogs.{filename[:-3]}')

#@client.command()
#async def unban(ctx, *, member):
#	banned_users = await ctx.guild.bans()
#	member_name, member_descriminator = member.split('#')
#	for ban_entry in banned_users:
#		user = ban_entry.user
#		if(user.name, user.descriminator) == (member_name, member_descriminator):
#			await ctx.guild.unban(user)
#			await ctx.send(f"Unbanned {user.mention}")
#			return

#@client.command(name='test', help='Test Command')
#async def test(ctx):
#	embed=discord.Embed(title='test', description='Yeet', colour=discord.Colour.blue())
#	embed.add_field(name='Test', value=f'Test text here')
#	await ctx.send(embed=embed)

client.run(TOKEN)
