import discord
import os
from keep_alive import keep_alive 
import discord

from discord.ext import commands, tasks
import asyncio
client = commands.Bot(command_prefix=["!"], case_insensitive=True)

@client.event
async def on_message(message):
        if message.channel.id == 861520164369465355:
            if message.author.id==874184247731171348 or message.author.id ==  947365454828150854 :  #collecter bots id.. i used 2 different
                a=str(message.content)
                if "nakano" in a or "968889203599483050" in a or "557578041908396033" in a or "Legendary" in a or "Epic" in a: 
                  if "1️⃣" in a or ":one" in a:
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:ba:952609199047708723>")
                      
                  if "2️⃣" in a or ":two" in a:
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:do:952609199039320204>")
                  if "3️⃣" in a or ":three"  in a :
                      await asyncio.sleep(0.34)
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:ga:952609199316152340>")

                  if "4️⃣" in a or ":four" or " <four:955631851119214663>" in a:
                      await asyncio.sleep(0.45)
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:ne:952609199936913488>")
                else:
                  if "1️⃣" in a or ":one" in a:
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:one_:911645406251876362>")
                  if "2️⃣" in a or ":two" in a:
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:two_:911645502058151936>")
                  if "3️⃣" in a or ":three"  in a :
                      await asyncio.sleep(0.34)
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:THREE_:911645626293448755>")

                  if "4️⃣" in a or ":four" or " <four:955631851119214663>" in a:
                      await asyncio.sleep(0.45)
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:MikuPing:893311534594412594>")
                if  "557578041908396033" in a:
                  if "1️⃣" in a or ":one" in a:
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:one_:911645406251876362>")
                  if "2️⃣" in a or ":two" in a:
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:two_:911645502058151936>")
                  if "3️⃣" in a or ":three"  in a :
                      await asyncio.sleep(0.34)
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:THREE_:911645626293448755>")

                  if "4️⃣" in a or ":four" or " <four:955631851119214663>" in a:
                      await asyncio.sleep(0.45)
                      message = await message.channel.fetch_message(message.reference.message_id)
                      await message.add_reaction("<:MikuPing:893311534594412594>")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
keep_alive()
client.run("####")#token
