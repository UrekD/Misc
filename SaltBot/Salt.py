#Source https://git.urek.eu
import asyncio
from colorama import Fore, Style
import datetime
import json
import httpx
import aiofiles
import os
import nextcord
import aiohttp
from nextcord.ext import commands, menus
import nextcord
from dotenv import load_dotenv
from nextcord import Embed
import psutil
import threading
import time
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
where = int(os.getenv('where')) 
url = os.getenv('webhook')

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_disconnect(self):
        now = datetime.datetime.now()
        print(now.strftime(f"{Fore.MAGENTA}[DISCONNECTED] {Style.RESET_ALL}%H:%M:%S "))

    async def on_resumed(self):
        now = datetime.datetime.now()
        print(now.strftime(f"{Fore.MAGENTA}[RESUME] {Style.RESET_ALL}%H:%M:%S "))

    async def on_ready(self):
        x = "git.urek.eu"
        await bot.change_presence(activity=nextcord.Game(name=x))
        now = datetime.datetime.now()
        print(now.strftime(f'{Fore.MAGENTA}[INFO] %H:%M:%S {Fore.RED}{bot.user}{Style.RESET_ALL} has connected to nextcord!'))

    async def my_background_task(self,LA):
        await self.wait_until_ready()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id==where:
            if message.author.bot==False:
                print(message.content)
                if message.attachments==[]:
                    await send_to_webhook(message)
                else:
                    for x in message.attachments:
                        await pic(message,x.url)
                    if message.content!="":
                      await send_to_webhook(message)

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        if before.channel.id==where:
            embed = nextcord.Embed(timestamp=before.created_at) 
            embed.set_author(name=f'{after.author.name}#{after.author.discriminator}', icon_url=after.author.display_avatar)
            embed.set_footer(text=f"Author ID:{after.author.id} • Message ID: {after.id}")
            embed.add_field(name="Member", value=f"<@{after.author.id}>", inline=True)
            embed.add_field(name="Channel", value=f"<#{after.channel.id}>", inline=True)
            embed.add_field(name="Message content before edited", value=before.content, inline=False)
            embed.add_field(name="Message content after edited", value=after.content, inline=False)
            #embed.add_field(name="Jump URL", value=before.jump_url, inline=False)
            await webhookembed(embed=embed)

async def webhookembed(embed):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(url, session=session)
        await webhook.send(embed=embed)

async def pic(message,x):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(url, session=session)
        await webhook.send(x, username=str(message.author),avatar_url=message.author.display_avatar)
        #await message.delete()

async def send_to_webhook(message):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(url, session=session)
        await webhook.send(message.content, username=str(message.author),avatar_url=message.author.display_avatar)
        #await message.delete()



intents = nextcord.Intents(message_content=True, messages=True, guilds=True)
bot = Bot(intents=intents)
bot.remove_command('help')

@bot.slash_command(name="threadds", description="Monitor time and when it last ran")
async def threadds(interaction: nextcord.Interaction):
    await interaction.response.defer()
    th = []
    for thread in threading.enumerate(): 
        th.append(thread.name)
    await interaction.followup.send((th,'RAM memory % used:', psutil.virtual_memory()[2],' The CPU usage is: ', psutil.cpu_percent(4)))
while True:
 try:
    bot.run(TOKEN,reconnect=True)
 except:
    time.sleep(10)
    os.system("kill 1")
