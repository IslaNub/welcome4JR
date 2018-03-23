import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

class liquidwelcome:
    """Welcomes new members to the server in the default channel"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        c = self.bot.get_channel('389100476630695946')
        m = 'Hello {}! Welcome to the Official Team Liquid Mobile Discord server. We hope you have a good time here.\nPlease add the role for the game you play (+ClashRoyale, +AoV, +BrawlStars).\nFor anything tag an online moderator or DM Liquid Mail if you have any questions.'
        await self.bot.send_message(c, m.format(member.mention))
        m2 ='Hello and welcome to Team Liquid\'s Mobile empire. Please review our new member pamphlet @ https://bit.ly/2px9czy for an introduction to Team Liquid and information on our mobile teams. \n\nIf you are currently in the Team Liquid Mobile empire or you would like to join then please fill out our official member registration located @ https://goo.gl/6kGVPZ - \n\nIf you have any questions then please join one of our community chats or reach out to a Discord moderator'
        await self.bot.send_message(member, m2)
        
    async def on_member_remove(self, member):
        c = self.bot.get_channel('414894603947343882')
        m = '{} has just left the Server, bye bye...'
        await self.bot.send_message(c, m.format(member.name))
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)

