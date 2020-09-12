import discord
import random
from discord.ext import commands

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '!')

client.remove_command('help')

@client.command()
async def wholesome(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

@client.command()
async def meme(ctx):
    responses = open('memes.txt').read().splitlines()
    random.seed(a=None)
    response = './memes/'+random.choice(responses)
    await ctx.send(file=discord.File(response))

@client.command()
async def ily(ctx):
    responses = open('ily.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

@client.command()
async def qt(ctx):
    await ctx.send(file=discord.File('./memes/14.jpg'))

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'({error}), use !help for usage')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='!wholesome', value='Responds with a wholesome quote :)', inline=False)
    embed.add_field(name='!meme', value='Posts a random whomesome meme <3', inline=False)
    embed.add_field(name='!all', value='List of all commands', inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def all(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red())
    embed.set_author(name='All commands of wholesomeBot')
    embed.add_field(name='!qt', value='Responds with you\'re a cutie meme ;)', inline=False)
    embed.add_field(name='!ily', value='Responds with an ily message <3', inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN)