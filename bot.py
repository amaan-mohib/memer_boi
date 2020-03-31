import discord
import praw
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import random

TOKEN='Njk0MDg1MTkzNjAyMDM5ODYy.XoLZyg.L3gzpZ1-A2KpUazBH_-D_AGvHRg'

client=discord.Client()

bot=commands.Bot(command_prefix='!')

# def run_client(client, *args, **kwargs):
#     loop = asyncio.get_event_loop()
#     while True:
#         try:
#             loop.run_until_complete(client.start(*args, **kwargs))
#         except Exception as e:
#             print("Error", e)  # or use proper logging
#         print("Waiting until restart")
#         time.sleep(600)

def reddit():
    reddit=praw.Reddit(client_id='aWeqij8e6gv9sg',client_secret='YPqKM4qXHP83dByowQWVuHkb5kw',user_agent='memer_boi')
    subreddit=reddit.subreddit('dankmemes')
    hot=subreddit.random()
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

@bot.command(name='meme')
async def meme(ctx):
    await ctx.send("Your meme "+ctx.message.author.mention+' <:point_down:694142240435601560>')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ctx.author.mention))
    url,title,link=reddit()
    print(url,title,link)
    val = random.randint(0, 0xFFFFFF)
    e=discord.Embed()
    e.set_image(url=url)
    e.color=val
    e.set_author(name=title,url=link)
    await ctx.send(embed=e)
    print('sent')

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('good') or message.content.startswith('Good'):
        msg = 'Thank you!'
        await message.channel.send(msg)
    await bot.process_commands(message)

bot.run(TOKEN)
