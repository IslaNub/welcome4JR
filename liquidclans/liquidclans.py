import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint
import asyncio
import requests
import aiohttp
from datetime import datetime
import time

tag = [" 9L928JQ"," G900CVQQ"," L8YJ8JGL"," Q28202UJ"," 88QGPCL"," Y9CJJG9U"," 28RCQ8U8V"," 2LPGCCVR8 ","2cjuyr8yr"," Q99QJ82J"," 29899VJLU"," L8PVPUPV"," 2RYGYOQ"," VCCQ28GY "," 2VUL9RGV"," 2UCLVL8"," 2PULU9VG"," 8800JYJ8"," jgurg9j"," 20PLU2"," P8YLG9VL"," 98200R0"," JJUCGVUG","YLQJCQ89"," 2V00VYP8L"," 88R0R08U"," 8GG8LL2Q"," R2Y9UYY"," LY8GGUU8"," GYGYUROC","900GYC08"," 2GR22209L"," 200QGCPGC"," 29CJQGQRR"," 2juy890"," YORG8L9Y"," YORG8L9Y"," 898LLGV0"," 82P0UUPPP"," 2YCRLPL8U"," Y20YQLYV"," 2VRRLGRR8","RPU8JUJO","LJ0228YC"," 2ccoorr","A7W0jM","8GLUQLG2"," 20PVJOQUL"," GGVRL22C"," 8QGUUY2L"," RRGJ9VUO"," P80C0J92"," 8YVRU8RG8"," PVP0YVVY"," 8QGUUY2L"," 2CQ9JYGG","n/a"," 8VLCVGLJ"," 8GYCLJ0L","A7W0jM"," 292VYLOO"," 2URVYU2Q"," 8q8009yl"," 2PLGCU2C9"," 8LJ0LVR8"," 29UJ9Q99"," 2L2GP29CQ"," 2L2GP29CQ","J0LY0c0y"," LV980V2Y"," YLJUPCPU"," 82C8OQCU"," PCPJUVC9"," 2RR2U2JGL "," YPCQRCJ"," 82L9PC2R0"," P898Q9R2"," L2QLPYVQ"," 2QLYOJC9R"," 2L8UCUQQP"," 2L8UCUQQP"," 88LRCUCY"," Y888YPRU"," 2J89YRC8"," Q929C2OL"," 2QY28CGL"," 29LY2RVPG"," 2CRU8VPPY"," 9L8PRGGC"," 9v8qgj"," 8Q8OCJOG"," vp9jq2r8"," 8P9JYLJL"," 808J28QV "," RUJYPYVJ"," 20YGQQPQL"," LY8VRCR9"," RQPQ0G8"," RL9GGCG"," 2VOL8RJ89"," Y80CV92"," 8P2VPQP8V"," PCULQJV2"," 8GU8RJLQ"," 2PQY08JL"," UCQL8Q29"," 2L98RV88U"," 2QPRQQU88"," PG0PC00L"," QGGCRPY8"," 299YUQL2V"," G99YUQG"," JUCGR8"," RPR8QRVL"," RCUO88QQ"," 88LQQY08"," GYGOUOU"," U2LYJV8R"," 89R2G0C9"," 8JLLLVUC"," 2l2jyoop"," 8JLLLVUC"," 8JLLLVUC"," 22PORP2LQ"," P2YL809"," PCJULYVQ"," 2PJGRRQL"," PJ0RC2LV"," 8QLGJCO"," 2CL90G9U"," 2POC88QGP "," P82VUU2P"," YG8CJV0Y"," 2PLYGR0PJ"," 8YVYG2CY"," 2999GUJ "," 8RYG0LLQ"," 9L2QJOJR","Main:QV28989 Second Account: 8UVQRRO8"," LQ2P98U "," 8VLLLLPU"," RPR8RRY9 "," 2VVU2CROP"," 8C0VPC92"," J2UOUGCP"," Y8008J08","2U22UR2C","9P0R8L02"," PLOUR2C9"," 899JRUY"," 8YUJOQLL"," 8C29J"," 20000YUG"," 89p8vu8p"," 8UQRPRCQ "," 82VCPRLRL"," UV8222GG"," PQLOPLUO"," 2RQLPL9VR"," QL8J92V2"," C80LG8Y"," 808220JQ"," Q8LRJPOP"," 8LLVVC2"," PYJQQUR8"," YY829PY2"," Q9PCVGPY"," 9G88ULGP"," QYCOUO"," 2JVRJQRU","JGJC00J"," YQCJJU99"," GQYG89VG"," 2JUCY9R8G"," R92QGOC"," LYU9C09J"," JJY0PRR8 "," 99YR2YPV"," LPJYQV0L"," 88C8VV0QV"," 82PQ2CVR"," 2L2GV20Y0"," 902L9LRU"," 2YLR2R9LO"  ]

APIAuth = {'auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQ3LCJpZGVuIjoiMTk5NDM2NzkwNTgxNTU5Mjk2IiwibWQiOnt9LCJ0cyI6MTUyODk5NjY1MjE5OX0.d3y3VSG1EOU_pOfFcFWTFEFH3U0BeOoME0TcChnQ__k'}
EUClans = ['98PYR0VJ', '9UP2JY2P', 'PQR8L08Y', 'P0YJ0P2V', 'P888QQQ9', '98R22PLY', '9QRU02GR', '9U82UYLJ', 'P0P2G8YQ', 'P09YPG9V', 'PY9QVRCJ', '8J0J2RQC', '9JUCLVCV', '9UYLCJYP']
MexicoClans = ['8URY28UC', '92J9RY9C', '8U0V8CG0', '9PPJJVLQ', '9Q88CP22']
HondurasClans = ['9LGV822C']
ElSalvadorClans = ['8JG8Y20R', '99UL0CRJ', '9YYGCYVL']
VenezuelaClans = ['VOGL8C8', '889CQU88', '8L98R2JV', '8R8LJYU2', '8J8UVQL0']
ColombiaClans = ['90Q0LP0V']
PeruClans = ['9YR8L8R8', '8JROLQ8U', '98LJJLR9', '8CPJV28G', '8G90Y22R', '9GLPUC2R', '980VLVOJ', 'P80J882L', '9LCUJC8Y', '9JL98G9J']
ParaguayClans = ['9LPC2YYV']
EcuadorClans = ['9GVUUCRR', 'P0PPQGY8']
ArgentinaClans = ['9P2CUYJR', 'P88LCUGQ'] 
NAClans = ['9YU2PQRV', 'V8GRLCQ', '9CJ9YGPL', '820QC80V', '9QVYYYV0', '9YYLQ99L']
LASClans = ['9QLLG92U', 'V0GL8C8', '889CQU88', '8R8LJYU2', '8J8UVQL0', '8L98R2JV', '8JR0LQ8U', '98LJJLR9', '8CPJV28G', '8G90Y22R', '9GLPUC2R', '980VLV0J', '9YR8L8R8', 'P80J882L', 'P22C00YR']
LANClans = ['8URY28UC', '92J9RY9C', '9PPJJVLQ', 'P2PP8L80', '9QL02L9U', '9LGV822C', '8JG8Y20R', '99UL0CRJ', '9LPJUVYJ']
 

class liquidclans:
    """Liquid Clans"""

    def __init__(self, bot):
        self.bot = bot
    
    def display_time(self, seconds, granularity=2):
        intervals = (
            ('weeks', 604800),  # 60 * 60 * 24 * 7
            ('days', 86400),    # 60 * 60 * 24
            ('hours', 3600),    # 60 * 60
            ('minutes', 60),
            ('seconds', 1),
        )

        result = []

        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return ', '.join(result[:granularity])
    
    @commands.has_permissions(administrator = True)
    @commands.command(pass_context = True, no_pm = True)
    async def trigger(self, ctx, region):
        eu = ['98R22PLY', '98PYR0VJ']
        x = 0
        if region.lower().strip() == 'eu':
            CRegion = EUClans
            reg = 'EU'
            c = self.bot.get_channel('450920001134657536')
            pass
        if region.lower().strip() == 'na':
            CRegion = NAClans
            reg = 'NA'
            c = self.bot.get_channel('450920685699858462')
            pass
        if region.lower().strip() == 'las':
            CRegion = LASClans
            reg = 'LAS'
            c = self.bot.get_channel('450920818260836352')
        if region.lower().strip() == 'lan':
            CRegion = LANClans
            reg = 'LAN'
            c = self.bot.get_channel('479774601765715968')
            #await self.bot.say('Not ready yet.')
            #return
        #c = self.bot.get_channel('447519506210750474')
        starter = await self.bot.send_message(c, '***__{} CLANS:__***'.format(reg))
        #await self.bot.send_message(c, '***__EU CLANS:__***')
        while True:
            try:
                while True:
                    clan = CRegion[x]
                    try:
                        headers = APIAuth
                        url = "https://api.royaleapi.com/clan/{}".format(clan)
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url, headers=headers) as resp:
                                data = await resp.json()
                                warurl = "https://api.royaleapi.com/clan/{}/war".format(clan)
                                async with session.get(warurl, headers = headers) as wresp:
                                    wdata = await wresp.json()
                                    pass
                                try:
                                    embed = discord.Embed(title = '', url = 'https://royaleapi.com/clan/{}'.format(clan), color = 0x00FFBF)
                                    embed.set_author(name = 'Stats for {}!'.format(data['name']))
                                    embed.title = f"{data['name']} (#{data['tag']})"
                                    embed.set_thumbnail(url = data['badge']['image'])
                                    embed.add_field(name = 'Description:', value = data['description'], inline = True)
                                    embed.add_field(name = 'Clan Points:', value = f"{data['score']} <:Trophy:443281867316264960>", inline = True)
                                    embed.add_field(name = 'Member Count:', value = f"{data['memberCount']}/50 <:Members:443282536764801026>", inline = True)
                                    embed.add_field(name = 'Required Trophies:', value = f"{data['requiredScore']} <:Trophy:443281867316264960>", inline = True)
                                    embed.add_field(name = 'Donations:', value = f"{data['donations']} <:Cards:443285942875193344>", inline = True)
                                    embed.add_field(name = 'Type:', value = f"{data['type']}".capitalize(), inline = True)
                                    embed.add_field(name = 'Location:', value = data['location']['name'], inline = True)
                                    if wdata['state'] == 'notInWar':
                                        state = 'Not currently in a Clan War'
                                        pass
                                    if wdata['state'] == 'warDay':
                                        seconds = abs(int(wdata['warEndTime']))
                                        dtime = self.display_time(seconds)
                                        state = 'War Day, ends in {} <:ClanWars:450674675140263936>'.format(dtime)
                                        pass
                                    if wdata['state'] == 'collectionDay':
                                        seconds = abs(int(wdata['collectionEndTime']))
                                        dtime = self.display_time(seconds)
                                        state = 'Collection Day, ends in {} <:Cards:443285942875193344>'.format(dtime)
                                        pass
                                    embed.add_field(name = 'War Status:', value = state, inline = True)
                                    if wdata['state'] in ['warDay', 'collectionDay']:
                                        embed.add_field(name = 'Clan War Participants:', value = str(len(wdata['participants'])) + ' <:Members:443282536764801026>', inline = True)
                                        pass
                                    embed.set_footer(text = 'LiquidClans v{} - API powered by RoyaleAPI'.format('1.0.2.1'), icon_url = 'https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')
                                    msg = await self.bot.send_message(c, embed = embed)
                                    x += 1
                                    if x >= len(CRegion):
                                        #await self.bot.send_message(c, 'Working')
                                        await asyncio.sleep(86400)
                                        lim = len(CRegion)
                                        async for message in self.bot.logs_from(c, limit = lim, after = starter):
                                            to_delete = [] 
                                            to_delete.append(message)
                                            x = 0
                                            await self.mass_purge(to_delete)
                                            pass
                                        await self.bot.delete_message(starter)
                                        starter = await self.bot.send_message(c, '***__{} CLANS:__***'.format(reg))
                                        pass
                                except Exception as e:
                                    x += 1
                                    #await self.bot.send_message(c, e)
                                    await self.bot.send_message(c, 'Something went wrong, please try again later.')
                                    print(e)
                                    pass
                    except Exception as e:
                        x = 0
                        #await self.bot.send_message(c, e) 
                        print(e)
            except Exception as e:
                x = 0
                #await self.bot.send_message(c, e)
            #await asyncio.sleep(10)
            #await self.bot.delete_message(msg)
            
    """@commands.command(pass_context = True, no_pm = True)
    async def triggerna(self, ctx):
        
        x = 0
        
        #await self.bot.say(len(eu))
        c = self.bot.get_channel('447519506210750474')
        starter = await self.bot.send_message(c, '***__NA CLANS:__***')
        #await self.bot.send_message(c, '***__EU CLANS:__***')
        while True:
            try:
                while True:
                    clan = NAClans[x]
                    try:
                        headers = APIAuth
                        url = "https://api.royaleapi.com/clan/{}".format(clan)
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url, headers=headers) as resp:
                                data = await resp.json()
                                try:
                                    embed = discord.Embed(title = '', url = 'https://royaleapi.com/clan/{}'.format(clan), color = 0x00FFBF)
                                    embed.set_author(name = 'Stats for {}!'.format(data['name']))
                                    embed.title = f"{data['name']} (#{data['tag']})"
                                    embed.set_thumbnail(url = data['badge']['image'])
                                    embed.add_field(name = 'Description:', value = data['description'], inline = True)
                                    embed.add_field(name = 'Clan Points:', value = f"{data['score']} <:Trophy:443281867316264960>", inline = True)
                                    embed.add_field(name = 'Member Count:', value = f"{data['memberCount']}/50 <:Members:443282536764801026>", inline = True)
                                    embed.add_field(name = 'Required Trophies:', value = f"{data['requiredScore']} <:Trophy:443281867316264960>", inline = True)
                                    embed.add_field(name = 'Donations:', value = f"{data['donations']} <:Cards:443285942875193344>", inline = True)
                                    embed.add_field(name = 'Type:', value = f"{data['type']}".capitalize(), inline = True)
                                    embed.set_footer(text = 'LiquidClans v{} - API powered by RoyaleAPI'.format('0.1'), icon_url = 'https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')
                                    embed.add_field(name = 'Location:', value = data['location']['name'], inline = True)
                                    
                                    msg = await self.bot.send_message(c, embed = embed)
                                    x += 1
                                    if x >= len(NAClans):
                                        #await self.bot.send_message(c, 'Working')
                                        await asyncio.sleep(3600)
                                        lim = len(NAClans)
                                        async for message in self.bot.logs_from(c, limit = lim, after = starter):
                                            to_delete = [] 
                                            to_delete.append(message)
                                            x = 0
                                            await self.mass_purge(to_delete)
                                            pass
                                        await self.bot.delete_message(starter)
                                        starter = await self.bot.send_message(c, '***__NA CLANS:__***')
                                            
                                        pass
                                    
                                except Exception as e:
                                    x = 0
                                    #await self.bot.send_message(c, e)
                                    await self.bot.send_message(c, 'Something went wrong, please try again later.')
                                    print(e)
                    except Exception as e:
                        x = 0
                        #await self.bot.send_message(c, e) 
                        print(e)
            except Exception as e:
                x = 0"""
                                                    
    async def mass_purge(self, messages):
        while messages:
            if len(messages) > 1:
                await self.bot.delete_messages(messages[:100])
                messages = messages[100:]
            else:
                await self.bot.delete_message(messages[0])
                messages = []
            await asyncio.sleep(1.5)
        
    @commands.command(pass_context = True, no_pm = True)
    async def testtrigger(self, ctx):
        c = self.bot.get_channel('414094090070786058')
        msg = await self.bot.send_message(c, "kek")
        while True:
            #c = self.bot.get_channel('414094090070786058')
            msg = await self.bot.send_message(c, "lol")
            
    @commands.command(pass_context = True, no_pm = True)
    async def wins(self, ctx):
        x = 0                                            
        while True:
            ptag = tag[x].strip()
            try:
                headers = APIAuth
                url = "https://api.royaleapi.com/player/{}".format(ptag)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as resp:
                        data = await resp.json()
                        #if data['stats']['challengeMaxWins'] >= 15:
                            #await self.bot.say('**' + data['name'] + ' (#' + str(data['tag']) + ')** has more than 15 Wins.')
                        if data['stats']['challengeMaxWins'] < 15:
                            await self.bot.say('**' + data['name'] + ' (#' + str(data['tag']) + ')** does NOT have more than 15 Wins.')                       
                        x += 1
                        if x >= len(tag):
                            await self.bot.say('I should have finished...🤔')                     
                            break                            
            except Exception as e:
                await self.bot.say('#' + ptag + ' is wrong.')
                x += 1                               
        
    @commands.command(pass_context = True, no_pm = True)
    async def testwins(self, ctx):
        x = 0                                            
        testtag = ['9L928JQ', 'G900CVQQ', 'PCVRL8GJ']                                            
        while True:
            ptag = testtag[x].strip()
            try:
                headers = APIAuth
                url = "https://api.royaleapi.com/player/{}".format(ptag)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as resp:
                        data = await resp.json()
                        if data['stats']['challengeMaxWins'] >= 15:
                            await self.bot.say('**' + data['name'] + ' (#' + str(data['tag']) + ')** has more than 15 Wins.')
                        elif data['stats']['challengeMaxWins'] < 15:
                            await self.bot.say('**' + data['name'] + ' (#' + str(data['tag']) + ')** does NOT have more than 15 Wins.')                       
                        x += 1
                        if x >= len(testtag):
                            await self.bot.say('I should have finished...🤔')                     
                            break                            
            except Exception as e:
                await self.bot.say(e)
                pass
                                                    
def setup(bot):
    n = liquidclans(bot)
    bot.add_cog(n)
