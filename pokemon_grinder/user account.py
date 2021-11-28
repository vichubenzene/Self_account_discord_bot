

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
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

 

import datetime
tip = datetime.datetime.now()
pip=("%s / %s / %s" % (tip.day, tip.month, tip.year))
top=("%s : %s : %s" % (tip.hour, tip.minute, tip.second))

from itertools import cycle


@client.event
async def on_message(message):
      if message.author.id == 869618880232947712:
            if message.guild.id==588021653464940554:
                name=str(message.channel)
                name = name.replace("-", " ")
                channel = client.get_channel(781832261921800225)
                if name=="porygon":
                    await channel.send(f",c {name}2")
                name=name.replace("mr","mr.")
                name=name.replace(" jr"," jr.")
                await channel.send(f",c {name}")
                if name.startswith('shadow'):
                    await channel.send(f",buy shadow balls")

@client.event
async def on_message_edit(before, after):
    await client.process_commands(after)

def RandomColor():
    randcolor = discord.Color(random.randint(0, 16777215))
    return randcolor


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

print(f'[SUCCESFULLY]  - Logged in as {client.user}.')

client.run(os.getenv('TOKEN'), bot=False)

