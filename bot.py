import random
import asyncio
import aiohttp
import json
import discord
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("")
TOKEN = "NDYzOTg1MjY2OTExMzQ2Njg4.DjTe8Q.HZk_wkGDBMWTaQPrnlu4j6rjRik"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

client.load_extension('igcommand')

@client.event
async def on_member_join(member):
    channel = member.server.get_channel("472097268158169119")
    await client.send_message(channel, 'Hey '+ member.mention+'! Enter help to know the list of command :) ')




@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)




client.run(TOKEN)
