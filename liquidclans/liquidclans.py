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
        
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)
