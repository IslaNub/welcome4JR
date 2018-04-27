import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint
import asyncio

class liquidwelcome:
    """Welcomes new members to Team Liquid Mobile"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        ser = self.bot.get_server('301578535175323658')
        #nv = discord.utils.get(ser.roles, name = 'Not Verified')
        cr = discord.utils.get(ser.roles, name = 'Clash Royale')
        bs = discord.utils.get(ser.roles, name = 'Brawl Stars')
        aov = discord.utils.get(ser.roles, name = 'Arena of Valor')
        cj = self.bot.get_channel('432157348371628042')
        mj = '**{}** has joined the Server! <:liquid3:425779102927290388>\n```{} members in the Server.```'.format(member.name, ser.member_count)
        await self.bot.send_message(cj, mj)
        await self.bot.add_roles(member, cr)
        await self.bot.add_roles(member, aov)
        await self.bot.add_roles(member, bs)                        
        #await self.bot.add_roles(member, nv)
        #c = self.bot.get_channel('432154053825265684')
        #m = '**Hello {}! Welcome to the Official Team Liquid Mobile Discord server.**\n\n<:tl:429889965397245964>Please look in <#429719437763936256> and add the role for the game you play.\n<:tl:429889965397245964>You must be a member in one of our official teams to have a member role.\n<:tl:429889965397245964>Check out our various channels for info on prizes, events, teams, and much more.\n<:tl:429889965397245964>Tag an online moderator or DM Liquid Mail if you have any questions.\n***__By clicking on the "✅" reaction you will get access to the Server and you declare that you have read the Server rules.__***'.format(member.mention)
        #emojis = ['✅']
        #ms = await self.bot.send_message(c, m)
        #for e in emojis:
        #    await self.bot.add_reaction(ms, e)
        #try:
        #    r, u = await self.bot.wait_for_reaction(emoji = emojis, user = member, message = ms, timeout = 600)
        #except TypeError:
        #    await self.bot.delete_message(ms) 
        #    await self.bot.remove_roles(member, nv)
        #    await self.bot.add_roles(member, dumb)
        #    await self.bot.remove_roles(member, nv)
        #else:
        #    if r.emoji == emojis[0]:
        #        await self.bot.delete_message(ms) 
        #        await self.bot.remove_roles(member, nv)
        
    async def on_member_remove(self, member):
        c = self.bot.get_channel('432157348371628042')
        s = self.bot.get_server('301578535175323658')
        m = '**{}** has left the Server, bye bye... <:QooBeeConsole:422749739591794688>\n```{} members left in the Server.```'.format(member, s.member_count)
        await self.bot.send_message(c, m)
        
    async def on_member_ban(self, member):
        c = self.bot.get_channel('432157348371628042')
        s = self.bot.get_server('301578535175323658')
        m = 'Someone has used the Hammer and **{}** has been banned from this Server! <:BanHammer:438979295671746560>'.format(member)
        await self.bot.send_message(c, m)
        
    @commands.command(pass_context = True, no_pm = True)
    async def liquid(self, ctx):
        """Team Liquid Mobile Information"""
        server = ctx.message.server
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        em = discord.Embed(colour=discord.Colour(value=colour))
        em.title = "Team Liquid Information"
        em.description = "Welcome to Team Liquid Mobile!"
        if server.icon_url:
            em.set_author(name=server.name, url=server.icon_url)
            em.set_thumbnail(url=server.icon_url)
        em.add_field(name="__GUIDE__", value="**Here is a brief guide to our server to get you started:**\n\n[Team Liquid Mobile New Member Pamphlet](https://bit.ly/2px9czy)\n[Team Liquid Mobile New Member Registration](https://goo.gl/6kGVPZ)\n\n[Team Liquid Mobile Academy Team Pamphlet](https://bit.ly/2uk38PI)\n[Team Liquid Mobile Academy Team Registration](https://bit.ly/2G7YTbA)")
        em.set_footer(text="Thanks for joining Liquid")
        await self.bot.say(embed=em)
        
    @commands.command(pass_context=True, no_pm=True)
    async def who(self, ctx):
        """Find out who is stupid!"""
        channel_id = ctx.message.channel.id
        owner = ctx.message.author
        message = 'Who is stupid?'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        ms = await self.bot.wait_for_message(check = lambda x : x.author == ctx.message.author)
        IslaNub = '199436790581559296'
        saka = '323543378509824002'
        isla = '<@199436790581559296>'
        if ctx.message.author.id == IslaNub:
            await self.bot.say(f'Oh, my Master! You\'re the brightest person I\'ve ever seen! You definitely are right! {ms.content} really is stupid!')
        elif ctx.message.author.id == saka:
            await self.bot.say(f'Awww saka, since Isla has faith in you I\'m pretty sure you\'re right, {ms.content} is pretty much stupid!')
        elif ms.content == isla:
            await self.bot.say('Idk')
        else:
            await self.bot.say('Are you sure? (yes/no)')
            answer1 = ('yes')
            answer2 = ('no')
            msg = await self.bot.wait_for_message(author=owner)
            if msg.content.lower().strip() in answer1:
                if ms.content == 'I':
                    await self.bot.send_message(self.bot.get_channel(channel_id), 'Indeed, you are! Btw it\'s "me", not "I"...')
                elif ms.content == 'You':
                    await self.bot.send_message(self.bot.get_channel(channel_id), 'I am smart enough to understand you tried to troll me... Believe me, the stupid here is you, not me!')
                else:
                    await self.bot.send_message(self.bot.get_channel(channel_id), f'Hmm perhaps, I\'m not sure if {ms.content} is stupid, but I\'m sure YOU are!')
            elif msg.content.lower().strip() in answer2:
                await self.bot.send_message(self.bot.get_channel(channel_id), 'Nice! You\'re right, because you\'re stupid!')
            else:
                await self.bot.send_message(self.bot.get_channel(channel_id), 'What don\'t you understand of "yes/no"??? Look how stupid...')

    @commands.command(pass_context = True, no_pm = True)
    async def msping(self, ctx):
        await self.bot.say(f'Pong! ({self.bot.ws.latency * 1000:.0f} ms)')

    @commands.command(pass_context = True, no_pm = True) 
    async def addacademy(self, ctx, user : discord.Member):
        """Adds Academy role to user."""
        ser = self.bot.get_server('301578535175323658')
        ac = discord.utils.get(ser.roles, id = '430495770014253056')
        s = discord.utils.get(ser.roles, id = '432550860229443594')
        ma = discord.utils.get(ser.roles, id = '430493433669353483')
        u = ctx.message.author
        if s in u.roles:
            await self.bot.add_roles(user, ma)
            await self.bot.say('Added "{}" role to {}.'.format(ma.name, user.mention))
        else:
            await self.bot.say('You don\'t have permissions to use this command.')
        
    @commands.command(pass_context = True, no_pm = True) 
    async def removeacademy(self, ctx, user : discord.Member):
        """Removes Academy role from user."""
        ser = self.bot.get_server('301578535175323658')
        ac = discord.utils.get(ser.roles, id = '430495770014253056')
        s = discord.utils.get(ser.roles, id = '432550860229443594')
        ma = discord.utils.get(ser.roles, id = '430493433669353483')
        u = ctx.message.author
        if s in u.roles:
            await self.bot.remove_roles(user, ma)
            await self.bot.say('Removed "{}" role from {}.'.format(ma.name, user.mention))
        else:
            await self.bot.say('You don\'t have permissions to use this command.')
 
    @commands.command(pass_context = True, no_pm = True)
    async def getpracticestats(self, ctx, message_ID = None):
        ID = message_ID
        c = self.bot.get_channel('430496334340947978')
        if message_ID is None:
            async for message in self.bot.logs_from(c, limit = 1, reverse = True):
                m = await self.bot.get_message(c, message.id)
                pass
        if message_ID is not None:
            m = await self.bot.get_message(c, ID)
            pass
        try:
            r = await self.bot.get_reaction_users(discord.Reaction(emoji = '✅', message = m))
            x = 0
            ser = ctx.message.server
            s = discord.utils.get(ser.roles, id = '432550860229443594')
            acs = discord.utils.get(ser.roles, id = '430495770014253056')
            u = ctx.message.author
            if s in u.roles or acs in u.roles:
                m = await self.bot.say(r[x].name)
                while True:
                    try:
                        x += 1
                        m = await self.bot.edit_message(m, f'{m.content}\n{r[x].name}')
                    except Exception:
                        break
                await self.bot.say('**{} users have reacted.**'.format(len(r)))
            else:
                await self.bot.say('You are not allowed to use this command, only {} can.'.format(s.name))
        except Exception as e:
            await self.bot.say(e)
            print(e)
            
    @commands.command(pass_context = True, no_pm = True)
    async def testgetpracticestats(self, ctx, message_ID = None):
        ID = message_ID
        c = self.bot.get_channel('430496334340947978')
        if message_ID is None:
            async for message in self.bot.logs_from(c, limit = 1, reverse = True):
                m = await self.bot.get_message(c, message.id)
                pass
        if message_ID is not None:
            m = await self.bot.get_message(c, ID)
            pass
        try:
            x = 0
            ser = ctx.message.server
            s = discord.utils.get(ser.roles, id = '432550860229443594')
            acs = discord.utils.get(ser.roles, id = '430495770014253056')
            u = ctx.message.author
            if s in u.roles or acs in u.roles:
                await self.bot.say('For which region do you need stats?')
                try:
                    a = await self.bot.wait_for_message(author = u, timeout = 15)
                    if a.content.lower().strip() == 'eu':
                        r = await self.bot.get_reaction_users(discord.Reaction(emoji = '🇪🇺', message = m))
                        pass
                    if a.content.lower().strip() == 'na':
                        r = await self.bot.get_reaction_users(discord.Reaction(emoji = '🇺🇸', message = m))
                        pass
                except Exception:
                    await self.bot.say('Canceling operation.')
                m = await self.bot.say(r[x].name)
                while True:
                    try:
                        x += 1
                        m = await self.bot.edit_message(m, f'{m.content}\n{r[x].name}')
                    except Exception:
                        break
                if len(r) > 1:
                    plural = 's'
                    pass
                if len(r) <= 1:
                    plural = ''
                    pass
                await self.bot.say('**{} user{} have reacted.**'.format(len(r), plural))
            else:
                await self.bot.say('You are not allowed to use this command, only {} can.'.format(s.name))
        except Exception as e:
            print(e)
            
    @commands.group(pass_context=True, no_pm=True)
    async def mem(self, ctx):
        """Gives EU, NA or LA member to users
        
        Only Leaders can use this command"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            
    @mem.command(pass_context = True, no_pm = True, name = 'eu')
    async def mem_eu(self, ctx, member:discord.Member):
        try:
            eul = discord.utils.get(ser.roles, name = 'EU Clan Leader')
            eu = discord.utils.get(ser.roles, name = 'EU Clan Member')
            u = ctx.message.author
            x = eu
            if eul in u.roles:
                await self.bot.add_roles(member, x)
                await self.bot.say('Added {} role to {}.'.format(x.name, member.name))
            else:
                await self.bot.say('You need the {} role, your current highest role is {}.'.format(x.name, member.top_role))
        except Exception as e:
            await self.bot.say(e)
                                   
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)

    
    
