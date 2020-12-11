import discord
from discord.ext import commands, tasks
import random
from random import choice


Agents = ['Sova', 'Phoenix', 'Sage', 'Jett', 'Omen', 'Raze', 'Killjoy', 'Breach', 'Brimstone', 'Viper', 'Cypher',
          'Skye', 'Reyna']

status = ['Sleeping!', 'Jamming out to music!', 'Online!', 'Surfing the ocean', 'Rawr', 'who knows what']

client = commands.Bot(command_prefix='r!')
client.remove_command('help')

players = {}


@client.event
async def on_ready():
    change_status.start()
    print("RexBot is up!")


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('rex'):
        await message.channel.send(':t_rex: RAWR! :t_rex:')

    elif message.content.startswith('scrat'):
        await message.channel.send(':musical_keyboard::musical_keyboard: Piano! :musical_keyboard::musical_keyboard:')

    elif message.content.startswith('astro'):
        await message.channel.send(':teddy_bear: **djungelskog** :teddy_bear:')

    elif message.content.startswith('max'):
        await message.channel.send('choke me like you hate me but you love me🙈🥵😚')

    elif message.content.startswith('pie'):
        await message.channel.send('qt')

    elif message.content.startswith('yoshi'):
        await message.channel.send('yoshi is a dumbo')

    await client.process_commands(message)


@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(f'Pong! {round(latency * 1000)} ms')


@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.red()
    )

    embed.set_author(name='Help commands')
    embed.add_field(name='r!help', value='Brings up this help menu')
    embed.add_field(name='r!ping', value='Returns the latency of the server!', inline=False)
    embed.add_field(name='rex', value='Sends a fun message. - RAWR', inline=False)
    embed.add_field(name='r!agent', value='Picks a random Valorant agent', inline=False)
    embed.add_field(name='r!credits', value='Shows credits about the creator of the bot', inline=False)
    embed.add_field(name='r!8ball', value='This command is like 8ball, also knows as the ball of wisdom', inline=False)
    embed.add_field(name='r!coinflip', value='Flips a coin')
    await ctx.message.author.send(author, embed=embed)


@client.command()
async def agent(ctx):
    embed1 = discord.Embed(title='Agent Generator', description=str(random.choice(Agents)), colour=discord.Colour.red())
    await ctx.send(embed=embed1)


@client.command()
async def credits(ctx):
    await ctx.send('Made by `RexKB`')


@client.command(aliases=['8ball', 'magicball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def coinflip(ctx):
    choices = ['Heads', 'Tails']
    randcoin = random.choice(choices)
    await ctx.send(randcoin)


client.run('NjQzMTc3NDMzMzk0MzE1MzYz.XchrqQ.PPYQmSZdf0daJwdtjJp5hGg88mw')
