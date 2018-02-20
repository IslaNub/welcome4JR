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