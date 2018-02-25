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
        numbers = [1, 2, 3, 4]
        for n in numbers:
            emojis.append('{}⃣'.format(str(n)))
        message = 'Hello!! Welcome to the official Team Liquid discord server. Hope you have a great time here\n1. Want to join our TeamLiquid clans?\n2. Look at our clan list.\n3. Have any questions?\n4. Ask for a role'
        channel_id = '414095133294985221'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        for e in emojis:
            await self.bot.add_reaction(m, e)
            await asyncio.sleep(0.5)
        try:
            r, u = await self.bot.wait_for_reaction(emoji=emojis, user=member, message=m, timeout=480)
        except TypeError:
            await self.bot.clear_reactions(m)
            await self.bot.edit_message(m, 'Nuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuub.')
        else:
            await self.bot.clear_reactions(m)
            await self.bot.edit_message(m, 'Nuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuub.')
            if r.emoji == emojis[0]:
                await self.bot.send_message(u, 'U nub.')
            elif r.emoji == emojis[1]:
                pass
            elif r.emoji == emojis[2]:
                message = ('Beep boop.')
                channel_id = '414095133294985221'
                await self.bot.send_message(self.bot.get_channel(channel_id), message)
            elif r.emoji == emojis[3]:
                pass

def setup(bot):
    bot.add_cog(Welcome(bot))
