import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command(name='8ball', help='Replies to a question')
	async def eightball(self, ctx, *, question):
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
		embed=discord.Embed(title=f'8ball', 
			description=f'Get your questions answered by the almighty 8ball',
			colour=discord.Colour.red())
		embed.add_field(name=f'Question:', value=f'{question}')
		embed.add_field(name=f'Answer:', value=f'{random.choice(responses)}')
		embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=embed)
		#await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
	@eightball.error
	async def eightball_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(f'You need to give a question to be answered')

	@commands.command(name='roll_dice', aliases=['roll', 'rolldice'], 
		help='Simulates rolling dice. Enter the number of die and the number of sides as arg')
	async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
		dice = [
			str(random.choice(range(1, number_of_sides + 1)))
			for _ in range(number_of_dice)
		]
		embed=discord.Embed(title='Roll A Dice', 
			description=f'Rolling the good ol\' die', 
			colour=discord.Colour.dark_red())
		embed.add_field(name=f'Number of die:', value=f'{number_of_dice}')
		embed.add_field(name=f'Number of sides:', value=f'{number_of_sides}\n')

		embed.add_field(name=f'Result:', value=f', '.join(dice))
		embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=embed)
		#await ctx.send(', '.join(dice))
	@roll.error
	async def roll_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send(f'Arguments should be a number (integer)')
		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(f'A few arguments are missing. Please try again. The argument list is:\nnumber_of_dice number_of_sides')

	@commands.command(name='mirzapur', help='Responds with a random quote from Mirzapur')
	async def mirzapur(self, ctx):
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
		embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=embed)
    	#await ctx.send(response)
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Cog: Fun is online')

def setup(client):
	client.add_cog(Fun(client))
