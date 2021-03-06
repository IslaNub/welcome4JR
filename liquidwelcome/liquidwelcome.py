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

version = '0.2.2.6b'

TryoutMembers = ["Loader Beans#3355","qwe3rr#3277","ForgottenK#5736","JediBen#1959","Caleb#6483","GotMilk?#7432","Random#7563","King#5835","UltimateHunter#2164","ali-es10","Lime#3792","@Theoo Youtube⚽#7049 ","Trainer Asian #5861","⭐️ A I K E N ⭐️#3206","nakor#7277","Carterg_#1193","ajhernandez#9792","Kooze🌿🌚🌿#7130","CHOCO#0297","evan #9758","shaheer07#7354","kD77#6991","Azorty_QC#8678","bryn_norman ","ZUARTjose#8426","Zair#2399","Rumble98#1382","Fixitralph#8267","Eric Lopez Gonzalez#1341","lokesranger#1253","IXSAIDXI #1987","Jesus Peña#5940","PedroMan18#3866","pixelshoot*-*#0103","-Sergio-#0734","Legend MX#1540","SebasHB💎|Star Lord™#1186","LaloFeick❤#6713","Daddy#2240","Unicorn69 #6602","Alfreditogames#5180","DARKK-NIGHT#5754","cr254#7876","Jorge#1802","Marshmello#9994","Francisco08#0663","ifn9011CR 🇲🇽#6292","BRYAN CSE#8989","TheBiGBarbarian#5575","elgakkl#2953","Morrigan#4834","The Gocho#2678","LorDamteh❤#1215","Edwin U.#6691","ZEUScr#5102","By Neymar#5544","oreki walker#1938", "Ciper#0013","Miguel#7766","DabKing#6679","@red coder1👊#5632","Aurora | Strong#6846 ","chapulincolorao#6718","Alpha I Juan842 #1542","Superior#4140","Loris8700#6241","Yoann#9177","Luxus15 #0702","- NeozZ -#6075","Black Wolf#7512","Note#6942","Tøniø13#0927","Night Fighter#7322","Arttu#4798","Grey#5468","herthaChris #4195","Anis#7316","legamer#8901","Ad | !F¡N!T¥_₩♡rK#5474","Bodi#8128","Rey PEKKA#9315","ckJ#5399","Vatoloco503#3470","AYOUB#5969","MasterMind#2281","Emre Baltalı#1897","Elias#9146","#Åke1421","sheperd40 #1308","danieladamson#4164","Beast341#3984","HardcoreDennisCR#8734","ThugLife028#5621","Tomdehua#0047","Rocklibra#4606","radim cr#5306","Boom123 #1262","DarkKnight24#3584","Jose#3008","Pretoria Titan#3847","the thing2 #5174","merleyn#0387","Badaum|CR#4929","Lancelot#1082","#cosmaki4598","Hunter#2548 ","Striker#1905","Antoine34 #6282","KD.2Nova EG#9182 ","❎oscarinho❎#9703","NovaVikoMMG#5086","rondilla#8850","Schiwan#3164","JN#0376","Blankeart#3502","Bry™I不的#2968","suteekshan#7971","Andy#0719","Hardstone#8306","RohitFreaks#8709","Clan ToPPer#4874","King Zage#1769","Arcshaic#9484","IshaqNausherwani#5450","Abdullahaqeel#8007","OhhNOitsALEX#6289","VARTHAV™#1409","Synergy light #0036","TWISTEEER#0997","sachlang#8953","JH#3991","JO27#2944","blue dragon#0044","Anbelievable#6103"]

APIAuth = {'auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQ3LCJpZGVuIjoiMTk5NDM2NzkwNTgxNTU5Mjk2IiwibWQiOnt9LCJpYXQiOjE1MjYwMzEzMDd9.5caUvHM82sv4OZ7mxFsnZ20OZwx36QLGoJO93zMDBDQ'}
EUClans = ['98R22PLY', '98PYR0VJ', '9UP2JY2P', 'P0YJ0P2V', '8J0J2RQC', '9QRUO2GR', 'P888QQQ9']
MexicoClans = ['8URY28UC', '92J9RY9C', '8U0V8CG0', '9PPJJVLQ', '9Q88CP22']
HondurasClans = ['9LGV822C']
ElSalvadorClans = ['8JG8Y20R', '99UL0CRJ', '9YYGCYVL']
VenezuelaClans = ['VOGL8C8', '889CQU88', '8L98R2JV', '8R8LJYU2', '8J8UVQL0']
ColombiaClans = ['90Q0LP0V']
PeruClans = ['9YR8L8R8', '8JROLQ8U', '98LJJLR9', '8CPJV28G', '8G90Y22R', '9GLPUC2R', '980VLVOJ', 'P80J882L', '9LCUJC8Y', '9JL98G9J']
ParaguayClans = ['9LPC2YYV']
EcuadorClans = ['9GVUUCRR', 'P0PPQGY8']
ArgentinaClans = ['9P2CUYJR', 'P88LCUGQ'] 
NAClans = ['9YU2PQRV', 'V8GRLCQ', '9CJ9YGPL', '820QC80V']

class liquidwelcome:
    """Welcomes new members to Team Liquid Mobile"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        if member.server.id == '301578535175323658':
            ser = self.bot.get_server('301578535175323658')
            #nv = discord.utils.get(ser.roles, name = 'Not Verified')
            cr = discord.utils.get(ser.roles, name = 'Clash Royale')
            bs = discord.utils.get(ser.roles, name = 'Brawl Stars')
            aov = discord.utils.get(ser.roles, name = 'Arena of Valor')
            cj = self.bot.get_channel('432157348371628042')
            mj = '**{}** (`{}`) has joined the Server! <:LiquidWhite:454153267686014976>\n```{} members in the Server.```'.format(member.name, member.id, ser.member_count)
            await self.bot.send_message(cj, mj)
        #await self.bot.add_roles(member, cr)
        #await self.bot.add_roles(member, aov)
        #await self.bot.add_roles(member, bs)                        
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
        if member.server.id == '301578535175323658':
            c = self.bot.get_channel('432157348371628042')
            s = self.bot.get_server('301578535175323658')
            m = '**{}** (`{}`) has left the Server, bye bye... <:PandaNotLike:428559664733618176>\n```{} members left in the Server.```'.format(member, member.id, s.member_count)
            await self.bot.send_message(c, m)
        
    async def on_member_ban(self, member):
        if member.server.id == '301578535175323658':
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
        """Allows EU Leaders to add EU Member to users"""
        try:
            ser = ctx.message.server
            l = discord.utils.get(ser.roles, name = 'EU Clan Leader')
            eu = discord.utils.get(ser.roles, name = 'EU Clan Member')
            u = ctx.message.author
            x = eu
            if l in u.roles:
                await self.bot.add_roles(member, x)
                await self.bot.say('Added {} role to {}.'.format(x.name, member.name))
            else:
                await self.bot.say('You need the {} role to use this command, your current highest role is {}.'.format(l.name, member.top_role))
        except Exception as e:
            await self.bot.say(e)

    @mem.command(pass_context = True, no_pm = True, name = 'na')
    async def mem_na(self, ctx, member:discord.Member):
        """Allows NA Leaders to add NA Member to users"""
        try:
            ser = ctx.message.server
            l = discord.utils.get(ser.roles, name = 'NA Clan Leader')
            na = discord.utils.get(ser.roles, name = 'NA Clan Member')
            u = ctx.message.author
            x = na
            if l in u.roles:
                await self.bot.add_roles(member, x)
                await self.bot.say('Added {} role to {}.'.format(x.name, member.name))
            else:
                await self.bot.say('You need the {} role to use this command, your current highest role is {}.'.format(l.name, member.top_role))
        except Exception as e:
            await self.bot.say(e)
            
    @mem.command(pass_context = True, no_pm = True, name = 'la')
    async def mem_la(self, ctx, member:discord.Member):
        """Allows LA Leaders to add LA Member to users"""
        try:
            ser = ctx.message.server
            l = discord.utils.get(ser.roles, name = 'LA Clan Leader')
            la = discord.utils.get(ser.roles, name = 'LA Clan Member')
            u = ctx.message.author
            x = la
            if l in u.roles:
                await self.bot.add_roles(member, x)
                await self.bot.say('Added {} role to {}.'.format(x.name, member.name))
            else:
                await self.bot.say('You need the {} role to use this command, your current highest role is {}.'.format(l.name, member.top_role))
        except Exception as e:
            await self.bot.say(e)
            
    def getAuth(self):
        return {'auth' : '2da0f327dd7f41c7b0d87fae844fc3f24bc7c9ad99d44a7b9bc61f9cd76600dd'}
    
    #def EUClans(self):
    #    return ['98R22PLY', '98PYR0VJ', '9UP2JY2P', 'P0YJ0P2V', '8J0J2RQC', '9QRUO2GR', 'P888QQQ9']
    
    @commands.command(pass_context = True, no_pm = True)
    async def liquidclans(self, ctx, region:str):
        """Choose between EU, NA and LA
        
        
        LiquidClans v0.2.2.6b
        NOTE: This is a beta function, the code is still under development."""
        x = 0
        while True:
            try:
                if region.lower().strip() == 'eu':
                    clan = EUClans[x]
                    x += 1
                    
                elif region.lower().strip() == 'na':
                    clan = NAClans[x]
                    x += 1
                    pass
                elif region.lower().strip() == 'la':
                    if x == 0:
                        await self.bot.say('Please specify a country.\n```(Available: Mexico, Honduras, ElSalvador, Venezuela, Colombia, Peru, Paraguay, Ecuador, Argentina)```')
                        answer = await self.bot.wait_for_message(author = ctx.message.author, timeout = 15)
                    if x >= 0:
                        if answer.content.lower().strip() == 'mexico':
                            clan = MexicoClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'honduras':
                            clan = HondurasClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'elsalvador' or answer.content.lower().strip() == 'el salvador':
                            clan = ElSalvadorClans[x]
                            pass
                        elif answer.content.lower().strip() == 'venezuela':
                            clan = VenezuelaClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'colombia':
                            clan = ColombiaClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'peru':
                            clan = PeruClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'paraguay':
                            clan = ParaguayClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'ecuador':
                            clan = EcuadorClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() == 'argentina':
                            clan = ArgentinaClans[x]
                            x += 1
                            pass
                        elif answer.content.lower().strip() not in ['mexico', 'honduras', 'elsalvador', 'venezuela', 'colombia', 'peru', 'paraguay', 'ecuador', 'argentina']:
                            await self.bot.say('Invalid country, canceling operation.')
                            return
                        pass
                    pass
                elif region.lower().strip() not in ['eu', 'na', 'la']:
                    await self.bot.say('Invalid region: please choose `eu`, `na` or `la`.')
                    return
                try:
                    headers = APIAuth
                    url = "https://api.royaleapi.com/clan/{}".format(clan)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url, headers=headers) as resp:
                            data = await resp.json()
                            try:
                                await self.bot.send_typing(ctx.message.channel)
                                embed = discord.Embed(title = '', url = 'https://royaleapi.com/clan/{}'.format(clan), color = 0x00FFBF)
                                embed.set_author(name = 'Stats for {}!'.format(data['name']))
                                embed.title = f"{data['name']} (#{data['tag']})"
                                embed.set_thumbnail(url = data['badge']['image'])
                                embed.add_field(name = 'Description:', value = data['description'], inline = True)
                                embed.add_field(name = 'Clan Points:', value = f"{data['score']} <:Trophy:443281867316264960>", inline = True)
                                embed.add_field(name = 'Member Count:', value = f"{data['memberCount']}/50 <:Members:443282536764801026>", inline = True)
                                embed.add_field(name = 'Required Trophies:', value = f"{data['requiredScore']} <:Trophy:443281867316264960>", inline = True)
                                embed.add_field(name = 'Donations:', value = f"{data['donations']} <:Cards:443285942875193344>", inline = True)
                                embed.add_field(name = 'Type:', value = f"{data['type']}".capitalize(), inline = True)
                                embed.set_footer(text = 'LiquidClans v{} - API powered by RoyaleAPI'.format(version), icon_url = 'https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')
                                embed.add_field(name = 'Location:', value = data['location']['name'], inline = True)
                                #await self.bot.send_typing(ctx.message.channel)
                                await self.bot.say(embed = embed)
                            except Exception as e:
                                await self.bot.say(e)
                                await self.bot.say('Something went wrong, please try again later.')
                                print(e)
                except Exception as e:
                    await self.bot.say(e) 
                    print(e)
            except Exception as e:
                break
                await self.bot.say(e)
                
    @commands.has_permissions(ban_members = True)
    @commands.command(pass_context = True, no_pm = True)
    async def clanmembers(self, ctx, clan):
        if clan.lower().strip() == 'teamliquidger':
            clan = '98R22PLY'
            pass
        if clan.lower().strip() == 'teamliquidfr':
            clan = '98PYR0VJ'
            pass
        if clan.lower().strip() == 'flflourfr':
            clan = '9UP2JY2P'
            pass
        if clan.lower().strip() == 'teamliquidbl':
            clan = 'P0YJ0P2V'
            pass
        if clan.lower().strip() == 'teamliquidgsrb':
            clan = '8J0J2RQC'
            pass
        if clan.lower().strip() == 'teamliquidita':
            clan = '9QRUO2GR' 
            pass
        if clan.lower().strip() == 'tlsolid':
            clan = 'P888QQQ9'
            pass
        headers = APIAuth
        url = "https://api.royaleapi.com/clan/{}".format(clan)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                data = await resp.json()
                x = 0
                m = await self.bot.say(f"```{data['members'][x]['rank']}. {data['members'][x]['name']} #{data['members'][x]['tag']} - {data['members'][x]['role'].capitalize()}```")
                while True:
                    try:
                        x += 1
                        m = await self.bot.edit_message(m, f"```{m.content.strip('```')}\n{data['members'][x]['rank']}. {data['members'][x]['name']} #{data['members'][x]['tag']} - {data['members'][x]['role'].capitalize()}```")
                    except Exception:
                        break
    
    async def on_message(self, message):
        msg = 'academy tryouts link'
        if message.content.lower().strip() == msg:
            m = '<https://goo.gl/forms/hfDacbsxcZLwDmTV2>'
            await self.bot.send_message(message.channel, m)
    
    @commands.has_permissions(administrator = True)
    @commands.command(pass_context= True, no_pm = True)
    async def addtryout(self, ctx):
        x = 0
        t = discord.utils.get(ctx.message.server.roles, name = 'Tryouts')                                               
        try:
                                                            
            while True:
                try:   
                    tm = TryoutMembers[x]                                    
                    m = ctx.message.server.get_member_named(tm)
                    
                    await self.bot.add_roles(m, t)                                    
                    await self.bot.say('Added Tryouts role to ' + m.mention)
                    x += 1                                    
                except Exception:
                    await self.bot.say(tm + ' is not in this Server or the provided name and/or discriminator are not correct.')  
                    x += 1                                    
                    pass
                if x >= len(TryoutMembers):
                    break                                        
        except Exception as e:
            await self.bot.say(e)
                                                      
                                                        
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)

    
    

    
    
