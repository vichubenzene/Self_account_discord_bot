
from keep_alive import keep_alive

import discord
import os
from discord.ext import commands,tasks

import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
import json

from urllib.request import Request, urlopen

rich_presence = "y"
password = "qwerty"
client = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True)

import datetime

import random
tip = datetime.datetime.now()
pip=("%s / %s / %s" % (tip.day, tip.month, tip.year))
top=("%s : %s : %s" % (tip.hour, tip.minute, tip.second))


 

def check(message):
        return message.author.id ==646937666251915264 and message.channel.id == 954614872572850306
    
@tasks.loop(seconds=2000)
async def drop():
    try:
        channel = client.get_channel(954614872572850306)
        # await channel.send("ghost ping <@!696106146427175073>", delete_after=2)
        await channel.send("kd")
        message = await client.wait_for('message', check=check, timeout=30)
        a=random.randint(1,3)
        await asyncio.sleep(5)
        if a ==1 :
            await message.add_reaction("1️⃣")
        elif a==2:
            await message.add_reaction("3️⃣")
        else:
            await message.add_reaction("2️⃣")
        
    except:
        pass

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    drop.start()

# keep_alive()
# client.run(os.getenv('fuck'), bot=False)


