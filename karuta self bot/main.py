import discord
from discord.ext import commands

import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
import webserver
from webserver import keep_alive

from urllib.request import Request, urlopen


keep_alive()
prefix = "!"
token = "##" #token
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)


client.remove_command('help')

@client.event
async def on_reaction_add(reaction,user):
            if user.id == 646937666251915264:
                if str(reaction.emoji) == "🍬":
                    await message.add_reaction("🍬")
                if str(reaction.emoji) == "🍫":
                    await message.add_reaction("🍫")
                    

    
print(f'[SUCCESFULLY]  - Logged in as {client.user}.')

client.run(token, bot=False)

