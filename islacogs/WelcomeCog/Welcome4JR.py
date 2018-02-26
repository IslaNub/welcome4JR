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
        message = f'Hello {member.mention}! Welcome to the Official Team Liquid discord server. Hope you have a great time here\n1. Want to join our Team Liquid Clans?\n2. Look at our Clan List.\n3. Have any questions?\n4. Ask for a role'
        channel_id = '389100476630695946'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        for e in emojis:
            await self.bot.add_reaction(m, e)
            await asyncio.sleep(0.5)
        try:
            r, u = await self.bot.wait_for_reaction(emoji=emojis, user=member, message=m, timeout=99999999999999999999)
        except TypeError:
            await self.bot.clear_reactions(m)
        else:
            await self.bot.clear_reactions(m)
            if r.emoji == emojis[0]:
                await self.bot.send_message(u, 'Thanks for your interest! Here is the Google Form to Liquid:\nhttps://docs.google.com/forms/d/e/1FAIpQLSdl65dcN6ROYdtMKCfR6C8_b6T-shOJTsmi0UY7juEAUutY1Q/viewform?usp=sf_link')
                await self.bot.edit_message(m, f'Sent Google Form in DM to {member.mention}.')
            elif r.emoji == emojis[1]:
                reg = '<#301578535175323658>'
                await self.bot.edit_message(m, f'{member.mention} check {reg} for a List with the Clans!')
            elif r.emoji == emojis[2]:
                ModMail = '<@413786880111542282>'
                await self.bot.edit_message(m, f'{member.mention} if you have any question regarding Liquid send a message in private to {ModMail}.')
            elif r.emoji == emojis[3]:
                r = discord.utils.get(member.server.roles, name='Visitors')
                await self.bot.add_roles(member, r)
                await self.bot.edit_message(m, f'Added Visitors Role to {member.mention}, you can ask for a Role here.')

def setup(bot):
    bot.add_cog(Welcome(bot))
