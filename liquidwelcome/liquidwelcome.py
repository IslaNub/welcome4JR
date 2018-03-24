import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint

class liquidwelcome:
    """Welcomes new members to Team Liquid Mobile"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        c = self.bot.get_channel('389100476630695946')
        m = 'Hello {}! Welcome to the Official Team Liquid Mobile Discord server. \nPlease join a chat channel and add the role for the game you play (+ClashRoyale, +AoV, +BrawlStars).\nYou must be a member in one of our official teams to have a member role.\nYou must be an elder, co-leader, or leader in one of our official teams to have a citizen role. \nCheck out our various channels for info on prizes, events, teams, and much more. \nTag an online moderator or DM Liquid Mail if you have any questions.'.format(member.mention)
        await self.bot.send_message(c, m)
        m2 ='Hello and welcome to Team Liquid\'s Mobile empire. Please review our new member pamphlet @ https://bit.ly/2px9czy for an introduction to Team Liquid and information on our mobile teams. \n\nIf you are currently in the Team Liquid Mobile empire or you would like to join then please fill out our official member registration located @ https://goo.gl/6kGVPZ - \n\nIf you have any questions then please join one of our community chats or reach out to a Discord moderator'
        await self.bot.send_message(member, m2)
        
    async def on_member_remove(self, member):
        c = self.bot.get_channel('414094090070786058')
        s = self.bot.get_server('301578535175323658')
        m = '**{}** has just left the Server, bye bye<:QooBeeConsole:422749739591794688>... {} members left in the Server'.format(member.name, s.member_count)
        await self.bot.send_message(c, m)
        
    @commands.command(pass_context = True, no_pm = True)
    async def liquid(self, ctx):
        """Liquid Info"""
        server = ctx.message.server
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        em = discord.Embed(colour=discord.Colour(value=colour))
        em.title = "Team Liquid Information"
        em.description = "Welcome to Team Liquid Mobile!"
        if server.icon_url:
            em.set_author(name=server.name, url=server.icon_url)
            em.set_thumbnail(url=server.icon_url)
        em.add_field(name="***__Guide__***", value="**Here is a brief guide to our server to get you started:**\n\n[Team Liquid Mobile New Member Pamphlet](https://bit.ly/2px9czy)\n[Team Liquid Mobile New Member Registration](https://goo.gl/6kGVPZ)\n\n[Team Liquid Mobile Academy Team Pamphlet](https://bit.ly/2uk38PI)\n[Team Liquid Mobile Academy Team Registration](https://bit.ly/2G7YTbA)")
        em.set_footer(text="Thanks for joining Liquid")
        await self.bot.say(embed=em)

def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)


    
