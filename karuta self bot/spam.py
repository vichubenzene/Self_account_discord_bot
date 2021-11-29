
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


tip = datetime.datetime.now()
pip=("%s / %s / %s" % (tip.day, tip.month, tip.year))
top=("%s : %s : %s" % (tip.hour, tip.minute, tip.second))





import random


import itertools
channels=itertools.cycle([909881776858611732,831783629419970600])
@tasks.loop(seconds=20)
async def spam():
    try:
        ticks = datetime.datetime.now()
        pin = ("%s/%s/%s" % (ticks.day,ticks.month, ticks.year))
        pon= ("%s:%s:%s" % (ticks.hour, ticks.minute, ticks.second))
        channel = client.get_channel(next(channels))
        # await channel.send("ghost ping <@!696106146427175073>", delete_after=2) # for ghost ping lol
        await channel.send(f"> ＢＥＮ乙ＥＮＥ spam center since `{pip}`  `{top}` **:** `{pin}`  `{pon}`")
    except:
        pass



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    spam.start()


print(f'[SUCCESFULLY]  - Logged in as {client.user}.')

keep_alive()
client.run(os.getenv('fuck'), bot=False)
