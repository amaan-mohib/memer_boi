import discord
import asyncio
import praw
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import io
import aiohttp
import random

TOKEN='Njk0MDg1MTkzNjAyMDM5ODYy.XoID8Q.BW8iqVY_S1ReyrLy9X37NCugpIM'

client=discord.Client()

bot=commands.Bot(command_prefix='!')

def reddit():
    # url_list=list()
    # title_list=list()
    # id_list=list()
    # items=dict()
    reddit=praw.Reddit(client_id='aWeqij8e6gv9sg',client_secret='YPqKM4qXHP83dByowQWVuHkb5kw',user_agent='memer_boi')
    subreddit=reddit.subreddit('dankmemes')
    hot=subreddit.random()
    # for submission in hot:
    #     url_list.append(submission.url)
    #     title_list.append(submission.title)
    #     id_list.append(submission.id)
    # for (title,url,id) in zip(title_list,url_list,id_list):
    #     items.update({title:[url,id]})

    # title,arr=random.choice(list(items.items()))
    # url=arr[0]
    # id=arr[1]
    url=hot.url
    title=hot.title
    title_scr=hot.title.lower().replace(' ','_')
    id=hot.id
    link='https://www.reddit.com/r/dankmemes/comments/'+id+'/'+title_scr
    return url,title,link
    
@bot.event
async def on_ready():
    print("The bot is ready!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='you'))

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('good') or message.content.startswith('Good'):
        msg = 'Thank you!'
        await message.channel.send(msg)

@bot.command()
async def meme(ctx):
    await ctx.send("Your meme "+ctx.message.author.mention+' <:point_down:694142240435601560>')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ctx.message.author.mention))
    url,title,link=reddit()
    print(url,title,link)
    val = random.randint(0, 0xFFFFFF)
    e=discord.Embed()
    e.set_image(url=url)
    e.color=val
    e.set_author(name=title,url=link)
    await ctx.send(embed=e)
    print('sent')

bot.run(TOKEN)
