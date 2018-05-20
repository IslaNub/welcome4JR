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

APIAuth = {'auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQ3LCJpZGVuIjoiMTk5NDM2NzkwNTgxNTU5Mjk2IiwibWQiOnt9LCJpYXQiOjE1MjYwMzEzMDd9.5caUvHM82sv4OZ7mxFsnZ20OZwx36QLGoJO93zMDBDQ'}
EUClans = ['98R22PLY', '98PYR0VJ', '9UP2JY2P', 'P0YJ0P2V', '8J0J2RQC', '9QRUO2GR', 'P888QQQ9']
MexicoClans = ['8URY28UC', '92J9RY9C', '8U0V8CG0', '9PPJJVLQ', '9Q88CP22']
HondurasClans = ['9LGV822C']
ElSalvadorClans = ['8JG8Y20R', '99UL0CRJ', '9YYGCYVL']
VenezuelaClans = ['VOGL8C8', '889CQU88', '8L98R2JV', '8R8LJYU2', '8J8UVQL0']
ColombiaClans = ['90Q0LP0V']
PeruClans = ['9YR8L8R8', '8JROLQ8U', '98LJJLR9', '8CPJV28G', '8G90Y22R', '9GLPUC2R', '980VLVOJ', 'P80J882L', '9LCUJC8Y', '9JL98G9J']
ParaguayClans = ['9LPC2YYV']
EcuadorClans = ['9GVUUCRR', 'P0PPQGY8']
ArgentinaClans = ['9P2CUYJR', 'P88LCUGQ'] 
NAClans = ['9YU2PQRV', 'V8GRLCQ', '9CJ9YGPL', '820QC80V']

class liquidclans:
    """Liquid Clans"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True, no_pm = True)
    async def triggereu(self, ctx):
        eu = ['98R22PLY', '98PYR0VJ']
        x = 0
        
        #await self.bot.say(len(eu))
        c = self.bot.get_channel('447519506210750474')
        await self.bot.send_message(c, '***__EU CLANS:__***')
        while True:
            try:
                while True:
                    clan = EUClans[x]
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
                                    if x >= len(EUClans):
                                        #await self.bot.send_message(c, 'Working')
                                        await asyncio.sleep(10)
                                        lim = len(EUClans) + 1
                                        async for message in self.bot.logs_from(c, limit = lim, reverse = True):
                                            to_delete = [] 
                                            to_delete.append(message)
                                            x = 0
                                            await self.mass_purge(to_delete)
                                            await self.bot.send_message(c, '***__EU CLANS:__***')
                                            pass
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
                x = 0
                #await self.bot.send_message(c, e)
            #await asyncio.sleep(10)
            #await self.bot.delete_message(msg)
            
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
            
            
        
def setup(bot):
    n = liquidclans(bot)
    bot.add_cog(n)
