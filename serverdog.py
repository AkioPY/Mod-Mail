import discord
from discord.ext import commands
from discord import Embed, Color
import asyncio 
import random

TOKEN = "..."
client = commands.Bot(command_prefix=commands.when_mentioned_or("."), case_insensitive=True)
client.remove_command("help")

'''
#Events
@client.event
async def on_ready():
    print("SERVER DOG is ready")
    while True:
        await client.change_presence(activity=discord.Game("DM me for help/report"))
        await asyncio.sleep(600)
'''
#Events
@client.event
async def status_task():
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game('DM me for help/report'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Chill Bus Discord'))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print('Server Dog is Online')
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            embed = Embed(color=discord.Color.green())
            embed.add_field(name="**ModMail Support**",
            value=f"User Mention: {message.author.mention}\nUsername: {message.author}\nUser ID: {message.author.id}\n\n**_Content_**\n{message.content}")
            await client.get_guild(679671356593274881).get_channel(779687010134523945).send(embed=embed)
        await client.process_commands(message)


#Commands
@client.command()
@commands.has_any_role("Staff", "Helper/moderator")
async def r(ctx, member : discord.Member, *, text):
    await ctx.message.delete()
    await member.send(text)
    value = random.randint(0, 0xffffff)
    em = discord.Embed(
        description = "<:agree:766575148035473418> Reply successfully sent to the mentioned user!\nSent by "+ctx.message.author.mention,
        color = value
    )
    em.add_field(name="Reply: ",value=text)
    await ctx.send(embed=em)

@r.error
async def r_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description = "<:disagree:766575353816678452> A problem occured while sending the message!",
            colour = discord.Colour.red()       
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_any_role("Staff", "Helper/moderator")
async def reply(ctx, member : discord.Member, *, text):
    await ctx.message.delete()
    await member.send(text)
    value = random.randint(0, 0xffffff)
    em = discord.Embed(
        description = "<:agree:766575148035473418> Reply successfully sent to the mentioned user!\nSent by "+ctx.message.author.mention,
        color = value
    )
    em.add_field(name="**Reply: ",value=text) 
    await ctx.send(embed=em)

@reply.error
async def reply_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description = "<:disagree:766575353816678452> A problem occured while sending the message!",
            colour = discord.Colour.red()       
        )
        await ctx.send(embed=embed)

@client.command()
@commands.has_any_role("Staff", "Helper/moderator")
async def report(ctx, member : discord.Member, *, text):
    await ctx.message.delete()
    await member.send(text)
    value = random.randint(0, 0xffffff)
    em = discord.Embed(
        description = "<:agree:766575148035473418> Reply successfully sent to the mentioned user!\nSent by "+ctx.message.author.mention,
        color = value
    )
    em.add_field(name="*Reply: ",value=text)
    await ctx.send(embed=em)

@report.error
async def report_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description = "<:disagree:766575353816678452> A problem occured while sending the message!",
            colour = discord.Colour.red()       
        )
        await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = Embed(color=discord.Color.lighter_grey())
    embed.add_field(name="**ModMail Help**", value="\nThe Prefix: `.`\nYou will get messages from the user in a specific channel and to reply to it you can use:\n`.r <@member> <msg>`\n`.reply <@member> <msg>`\n`.report <@member> <msg>`")
    embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/779687869186179072/2c88294a141d2b84b807a5ded46e2072.png?size=256", text="Use any of the above commands ^")    
    await ctx.send(embed=embed)

client.run((TOKEN), reconnect=True)
