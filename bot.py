import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("")
TOKEN = "NDYzOTg1MjY2OTExMzQ2Njg4.DjTe8Q.HZk_wkGDBMWTaQPrnlu4j6rjRik"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='hello',
                aliases=['hola', 'hi', 'hey'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'Hello','Hi','Whats Up','Hey','Hola',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='who',
                aliases=['who are you', 'who is this', 'who r u','who are you?', 'who is this?', 'who r u?' ],
                pass_context=True)
async def who(context):
    possible_responses = [
        'I am Duty Officer of IG',

    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='ig',
                aliases=['imperial', 'guard', 'imperial guard','alliance', 'about alliance', 'your alliance', 'what is ig', 'about ig' ],
                pass_context=True)
async def ig(context):
    possible_responses = [
        'Imperial Guard is an alliance of pnw.',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
@client.command(name='ol',
                aliases=['haha', 'hehe', 'hihi', 'hah', 'huh', 'hahah', 'hahaha','heheh','hehehe', 'lol'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'Why laughing?',
        'Do you try to abuse me',
        'hehe!'

    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
@client.command(name='tax',
                aliases=['tax rate'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'i dont know. Denia is tax lover. talk to him.'

    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)




@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)

