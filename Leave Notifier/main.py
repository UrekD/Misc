#Source https://git.urek.eu
import asyncio
from colorama import Fore, Style
import datetime
import os
import nextcord
from nextcord.ext import commands
import nextcord
from dotenv import load_dotenv
import psutil
import threading
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
where = int(os.getenv('where')) 
role = os.getenv('role')
crole = os.getenv('crole')

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
    async def on_member_remove(self, member):
        for x in member.roles:
            if x.id == int(crole):
                x = f'{member}|{member.nick} deserted! Joined: {member.joined_at} <@&{role}>'
                await bot.get_channel(where).send(x)

intents = nextcord.Intents(members=True, guilds=True)
bot = Bot(intents=intents)
bot.remove_command('help')

@bot.slash_command(name="threadds", description="Monitor time and when it last ran")
async def threadds(interaction: nextcord.Interaction):
    await interaction.response.defer()
    th = []
    for thread in threading.enumerate(): 
        th.append(thread.name)
    await interaction.followup.send((th,'RAM memory % used:', psutil.virtual_memory()[2],' The CPU usage is: ', psutil.cpu_percent(4)))

bot.run(TOKEN,reconnect=True)