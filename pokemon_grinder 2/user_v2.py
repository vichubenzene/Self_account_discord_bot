
import discord
from discord.ext import commands, tasks
client = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True)
client.remove_command('help')
import requests
import cv2

from os import listdir
import sys
import os
from os.path import isfile, join
import json
import re
from keep_alive import keep_alive

sad_words=["Added to Pokédex","Shiny"]
@client.event
async def on_message(message):
    if message.channel.id== 771270409051832320:
        if message.author.id == 669228505128501258:
            async for m in message.channel.history(limit=1):
                    try:
                        print(m.content)
                        if any(word in m.content for word in sad_words):
                            channel=client.get_channel(892072792202285107)
                            em = discord.Embed(title=message.guild,
                                            description=message.content,colour=discord.Colour.red())
                            await channel.send(embed=em)
                        embeds = m.embeds  # return list of embeds
                        for embed in embeds:
                            # if b="A wild pokémon has аppeаred!"
                            real=a=embed.to_dict()["image"]["url"]
                            print(a)
                            response = requests.get(a)
                            tip = "hellp"

                            file = open(f"classifier/{tip}.png", "wb")
                            file.write(response.content)
                            file.close()
                            img = cv2.imread(f"classifier/{tip}.png", cv2.IMREAD_COLOR)
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
                                        await message.channel.send(f".c {j}")
                                except:
                                    pass
                            if t==0:
                                    channel=client.get_channel(892072792202285107)
                                    await channel.send(f"unable to detect {real}")
                    except:
                        pass
    await client.process_commands(message)
from itertools import cycle
a=cycle([1,2])
@tasks.loop(seconds=1500)
async def spam():
    if next(a)==2:
        channel=client.get_channel(892072792202285107)
        await channel.send(f"auto restart mai 2 ")
        restart_bot()

@client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(client))
    spam.start()

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
@client.command()
async def restart(ctx):
        if ctx.message.author.id==557578041908396033:
                print("hi")
                await ctx.send("> **Restarting bot...**", delete_after=7.5)
                restart_bot()
keep_alive()

client.run(os.getenv('token'), bot=False)
