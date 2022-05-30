from keep_alive import keep_alive

import discord
import os
from discord.ext import commands, tasks

import asyncio

from urllib.request import Request, urlopen

client = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True)
client.remove_command('help')


#autocard collecter
@client.event
async def on_reaction_add(reaction, user):
        if reaction.message.channel.id==861520164369465355:
            if (user.id)==844046442046029824:
                if str(reaction.emoji) == "<:ba:952609199047708723>" :
                    await reaction.message.add_reaction("1️⃣")
                    await asyncio. sleep(0.31) 
                if str(reaction.emoji)=="<:do:952609199039320204>":
                    await reaction.message.add_reaction("2️⃣")
                    await asyncio. sleep(0.31)
                if str(reaction.emoji) == "<:ga:952609199316152340>" :
                    await asyncio. sleep(0.35)
                    await reaction.message.add_reaction("3️⃣")
                    await asyncio. sleep(0.31)
                if str(reaction.emoji) == "<:ne:952609199936913488>" :
                    await asyncio. sleep(0.6)
                    await reaction.message.add_reaction("4️⃣")




#event time collecter
# @client.event 
# async def on_reaction_add(reaction,user):
#        if user.id == 646937666251915264:
#               if str(reaction.emoji) == "🍬":
#                     await reaction.message.add_reaction("🍬")
#               if str(reaction.emoji) == "🍫":
#                     await reaction.message.add_reaction("🍫")
        #     if str(reaction.emoji) == "🌼" :
        #         await asyncio. sleep(1.2)
        #         await reaction.message.add_reaction( "🌼")
        #     if str(reaction.emoji) == "🌷" :
        #         await asyncio. sleep(1.2)
        #         await reaction.message.add_reaction("🌷")
        #     if str(reaction.emoji) == "💐" :
        #         await reaction.message.add_reaction("💐")

@client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(client))


print(f'[SUCCESFULLY]  - Logged in as {client.user}.')

    

client.run("##########", bot=False) #token

