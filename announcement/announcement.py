import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify
from copy import deepcopy
import asyncio
import logging
import os


class announcement:
    """Announcement"""

    def __init__(self, bot):
        self.bot = bot
        
    #@commands.group(pass_context=True, no_pm=True)
    #async def empire(self, ctx):
        #"""Empire"""
        #if ctx.invoked_subcommand is None:
            #await self.bot.send_cmd_help(ctx)
        

    @commands.command(pass_context = True, no_pm = True)
    async def empire(self, ctx):
        u = ctx.message.author
        ea = discord.utils.get(server.roles, name = 'Empire Announcement')
        if ea in u.roles:
            await self.bot.say('You already have this role.')
        elif ctx.message.channel.id == '423748512396738571':
            await self.bot.add_roles(u, ea)
            await self.bot.say(f'Added Empire Announcement role to {u.mention}')
        else:
            await self.bot.say('You cannot use this command.')
            
def setup(bot):
    n = announcement(bot)
    bot.add_cog(n)
