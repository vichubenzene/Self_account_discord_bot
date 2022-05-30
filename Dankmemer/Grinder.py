
from keep_alive import keep_alive

import discord

from discord.ext import commands,tasks

import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
import json


client = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True)

@tasks.loop(seconds=37)
async def beg():
    try:
        await channel.send("pls beg")
    except:
        pass

@tasks.loop(seconds=38)
async def hunt():
    try:
        await channel.send("pls hunt")
    except:
        pass
      
@tasks.loop(seconds=40)
async def fish():
    try:
        await channel.send("pls fish")
    except:
        pass

### can add any evnent that need single message *mention time delay and *mention message content
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    beg.start()
    fish.start()
    hunt.start()
    #these are example add more if you want with crt time delay
keep_alive()
client.run(os.getenv('fuck'), bot=False)
