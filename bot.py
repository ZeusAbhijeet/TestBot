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

@client.command(name='ping', aliases=['latency'], help='Pong!')
async def ping(ctx):
	embed=discord.Embed(title='Pong!', description=f'Ping = {round(client.latency * 1000)}ms', colour=discord.Colour.blue())
	await ctx.send(embed=embed)
	#await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(name='8ball', help='Replies to a question')
async def eightball(ctx, *, question):
	responses = ['It is certain.',
				 'It is decidedly so.',
				 'Without a doubt.',
				 'Yes - definitely.',
				 'You may rely on it.',
				 'As I see it, yes.',
				 'Most likely.',
				 'Outlook good.',
				 'Yes.',
				 'Signs point to yes.',
				 'Reply hazy, try again.',
				 'Ask again later.',
				 'Better not tell you now.',
				 'Cannot predict now.',
				 'Concentrate and ask again.',
				 "Don't count on it.",
				 'My reply is no.',
				 'My sources say no.',
				 'Outlook not so good.',
				 'Very doubtful.']
	embed=discord.Embed(title=f'8ball', description=f'Get your questions answered by the almighty 8ball',colour=discord.Colour.red())
	embed.add_field(name=f'Question:', value=f'{question}')
	embed.add_field(name=f'Answer:', value=f'{random.choice(responses)}')
	await ctx.send(embed=embed)
	#await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
@eightball.error
async def eightball_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'You need to give a question to be answered')

@client.command(name='clear', aliases=['purge', 'delete'], help='Clears the given amount of messages. Deletes 3 messages by default.')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
	deleted = await ctx.channel.purge(limit=amount+1)
	msg = await ctx.send(f'Deleted {len(deleted)} messages')
	await asyncio.sleep(5)
	await msg.delete()
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'You require Manage Messages Permission to run this command.')

@client.command(name='roll_dice', aliases=['roll', 'rolldice'], help='Simulates rolling dice. Enter the number of die and the number of sides as arg')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	embed=discord.Embed(title='Roll A Dice', description=f'Rolling the good ol\' die', colour=discord.Colour.dark_red())
	embed.add_field(name=f'Number of die:', value=f'{number_of_dice}')
	embed.add_field(name=f'Number of sides:', value=f'{number_of_sides}\n')

	embed.add_field(name=f'Result:', value=f', '.join(dice))
	await ctx.send(embed=embed)
	#await ctx.send(', '.join(dice))
@roll.error
async def roll_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send(f'Arguments should be a number (integer)')
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'A few arguments are missing. Please try again. The argument list is:\nnumber_of_dice number_of_sides')

@client.command(name='mirzapur', help='Responds with a random quote from Mirzapur')
async def mirzapur(ctx):
	mirzapur_quotes = [
		'Mata ji yahan hai, Behen yahan hai, Maa-Behen ek karne mein aasani hogi.',
		'Attack me bhi gun, defense me bhi gun, Hum banayenge Mirzapur ko Amrica!',
		'Neta banna hai toh Gundey paalo. Gundey mat bano.',
		'Darr ki yahi dikkat hai, ki kabhi bhi Khatam ho sakta hai.',
		'Suru majboori mein kiye the….. Ab maza aa raha hai.',
		'Guns ki maddad se darr nahi badhana hai, Darr ki maddad se guns badhani hai.',
		'Izzat nahi karte hain… Darte hain sab.',
		(
			'Chutiya hain tumhara ladka.'
			'Chutiya hain woh important nahi hai. Hamara ladka hai, Woh important hai.'
		),
		'Agli baar Munna Bhaiya ghar aaye… Zinda wapas hi nahi laute toh?',
		'Oh Bhosaadi waley Chacha. Rest kariye, varna Rest in Peace ho jaoge!',
		'Zindagi ho toh aisi ho, Zinda toh jhaatt ke baal bhi hain.',
	]
	response = random.choice(mirzapur_quotes)
	embed=discord.Embed(title=f'Mirzapur Quote', description=f'{response}', colour=discord.Colour.dark_red())
	await ctx.send(embed=embed)
    #await ctx.send(response)

@client.command()
async def kick(ctx, member : discord.Member, *, reason='None'):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}\nReason: {reason}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason='None'):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}\nReason: {reason}')

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
