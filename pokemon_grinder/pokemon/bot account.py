# # # # # # # # # # #
import discord
from discord.ext import commands, tasks
client = commands.Bot(command_prefix=["!"], case_insensitive=True)

import requests
import cv2
import sys
import os
sad_words=["Added to Pokéde","Shiny"]
from os import listdir
import os
from os.path import isfile, join
import json
import re
from keep_alive import keep_alive
@client.event
async def on_message(message):
    if message.channel.id== 891890221564698694:#poke spawn channel
      if message.author.id == 669228505128501258:#pokemon id
        if any(word in message.content for word in sad_words): #new pokemon will be diverted to this channel
            channel=client.get_channel(892072792202285107)
            em = discord.Embed(title=message.guild,
                            description=message.content,colour=discord.Colour.red())
            await channel.send(embed=em)
        embeds = message.embeds  # return list of embeds
        for embed in embeds:
            b=embed.to_dict()["title"]
            # if b="A wild pokémon has аppeаred!"
            real=a=embed.to_dict()["image"]["url"]
            print(a)
            response = requests.get(a)

            file = open(f"test.png", "wb")
            file.write(response.content)
            file.close()
            img = cv2.imread(f"test.png", cv2.IMREAD_COLOR)
            # onlyfiles = [f for f in os.listdir() if isfile(join("pokemon", f))]
            


            t=0
            for j in os.listdir():
                try:
                    img2 = cv2.imread(f"{j}", cv2.IMREAD_COLOR)
                    a=img==img2
                    if a.all():
                        print(j)
                        j=j[:-4]
                        j = j.replace("#", "")
                        j = j.replace(" - ", "")
                        pattern = r'[0-9]'

                        # Match all digits in the string and replace them with an empty string
                        j = re.sub(pattern, '', j)

                        name = 'Your Category Name'
                        category = discord.utils.get(message.guild.categories, name=name)

                        channel = await message.guild.create_text_channel(f'{j}', category=category)
                        # await message.guild.create_text_channel(f'{j}', position=21)
                        a=await channel.send(j)
                        t=1
                        await a.channel.delete()
                        break
                except:
                    pass
            if t==0:
                    channel=client.get_channel(892072792202285107)
                    await channel.send(f"unable to detect {real}")


    await client.process_commands(message)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



keep_alive()
client.run(os.getenv('fuck'))
