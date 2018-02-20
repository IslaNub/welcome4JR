import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio


class Welcome:
    """Welcomes new members to the server in the default channel"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/welcome/settings.json", "load")


    @commands.group(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_server=True)


async def on_member_join(self, member):
    emojis = [":one:",":two"] 
    message = 'welcome, please do shit' 
    channel_id = '414095133294985221'
    m = await self.bot.send_message(bot.get_channel(channel_id), message)
    for e in emojis:
        await self.bot.add_reaction(m, e) 
        await asyncio.sleep(0.5)
    try:
        r, u = await self.bot.wait_for_reaction(emoji=emojis, user=member, message=m, timeout=5)
    except asyncio.TimeoutError:
        await self.bot.clear_reactions(m)
    else:
        await self.bot.clear_reactions(m) 
        if r.emoji == emoji[0]:
            pass
        elif r.emoji == emoji[1]:

def check_folders():
    if not os.path.exists("data/welcome"):
        print("Creating data/welcome folder...")
        os.makedirs("data/welcome")

def check_files():
    f = "data/welcome/settings.json"
    if not fileIO(f, "check"):
        print("Creating welcome settings.json...")
        fileIO(f, "save", {})
    else: #consistency check
        current = fileIO(f, "load")
        for k,v in current.items():
            if v.keys() != default_settings.keys():
                for key in default_settings.keys():
                    if key not in v.keys():
                        current[k][key] = default_settings[key]
                        print("Adding " + str(key) + " field to welcome settings.json")
        fileIO(f, "save", current)

def setup(bot):
    check_folders()
    check_files()
    n = Welcome(bot)
    bot.add_listener(n.member_join,"on_member_join")
    bot.add_cog(n)
