import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio


class announcement:
    """Announcement"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(pass_context=True, no_pm=True)
    async def empire(self, ctx):
        """Empire"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
        
    @empire.command(pass_context = True, no_pm = True, name = 'announcement')
    async def empire_announcement(self, ctx):
        await self.bot.say('kek')
            
def setup(bot):
    n = announcement(bot)
    bot.add_cog(n)
