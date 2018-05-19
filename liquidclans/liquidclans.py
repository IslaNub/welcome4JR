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

class liquidclans:
    """Liquid Clans"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True, no_pm = True)
    async def liquidclans(self, ctx, region:str):
        """Choose between EU, NA and LA
        
        
        LiquidClans v0.2.2.6b
        NOTE: This is a beta function, the code is still under development."""
        x = 0
        while True:
            try:
                
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
                                embed.set_footer(text = 'LiquidClans v{} - API powered by RoyaleAPI'.format(version), icon_url = 'https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')
                                embed.add_field(name = 'Location:', value = data['location']['name'], inline = True)
                                await self.bot.say(embed = embed)
                            except Exception as e:
                                await self.bot.say(e)
                                await self.bot.say('Something went wrong, please try again later.')
                                print(e)
                except Exception as e:
                    await self.bot.say(e) 
                    print(e)
            except Exception as e:
                break
                await self.bot.say(e)
        
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)
