import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint
import asyncio
import aiohttp

class liquidwelcome:
    """Welcomes new members to Team Liquid Mobile"""

    def __init__(self, bot):
        self.bot = bot
        self.info_data = data.get('info')
        
    @property
    def clan(self):
        """Clan."""
        return self.info_data.get("clan", None)

    @commands.command(pass_context = True, no_pm = True)
    async def clan(self, ctx, clan_id):
        headers = {"auth": "2da0f327dd7f41c7b0d87fae844fc3f24bc7c9ad99d44a7b9bc61f9cd76600dd"}
        url = "https://api.royaleapi.com/clan/{}".format(clan_id)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                data = await resp.json()
