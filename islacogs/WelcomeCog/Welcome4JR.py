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

    async def on_member_join(self, member):
        emojis = []
        numbers = [1, 2]
        for n in numbers:
            emojis.append('{}⃣'.format(str(n)))
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
                pass

def setup(bot):
    bot.add_cog(Welcome(bot))
