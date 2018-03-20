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
        u = ctx.message.author
        c = self.bot.get_channel('423748512396738571')
        ea = discord.utils.get(server.roles, name = 'Empire Announcement')
        if ea in u.roles:
            await self.bot.say('You already have this role.)
        elif ctx.message.channel == c:
            await self.bot.add_roles(u, ea)
            await self.bot.say(f'Added Empire Announcement role to {u.mention}')
        else:
            await self.bot.say('You cannot use this command.')
            
def setup(bot):
    n = announcement(bot)
    bot.add_cog(n)
