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

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='!wholesome', value='Responds with a wholesome quote :)', inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN)