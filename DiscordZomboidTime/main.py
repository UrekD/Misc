from datetime import datetime
from pprint import pprint
import nextcord
from nextcord.ext import tasks, commands
import os
import re
from file_read_backwards import FileReadBackwards
import asyncio
from colorama import Fore, Style
import glob
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.info, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.getLogger('telethon').setLevel(level=logging.WARNING)
#logger = logging.getLogger(__name__)


TOKEN = os.getenv("TOKEN")
logPath = os.getenv("LOG_PATH")
if logPath is None or len(logPath) == 0:
    path = Path.home().joinpath("Zomboid/Logs")
    if path.exists():
        logPath = str(path)
    else:
        logging.debug("Zomboid log path not set and unable to find default")
        print("Zomboid log path not set and unable to find default")
        exit()

GUILDID = os.getenv("GUILDID")
BOTID = os.getenv("BOTID")
NAME = os.getenv("NAME")
CHID = os.getenv("CHID")

intents = nextcord.Intents(messages=False, guilds=True)
bot = commands.bot.Bot(intents=intents,command_prefix='!')


@bot.event
async def on_disconnect():
        now = datetime.now()
        print(now.strftime(f"{Fore.MAGENTA}[DISCONNECTED] {Style.RESET_ALL}%H:%M:%S "))
@bot.event
async def on_resumed():
        now = datetime.now()
        print(now.strftime(f"{Fore.MAGENTA}[RESUME] {Style.RESET_ALL}%H:%M:%S "))
@bot.event
async def on_ready():
        bot.add_cog(TimeSet(bot,logPath))
        now = datetime.now()
        print(
            now.strftime(
                f"{Fore.MAGENTA}[INFO] %H:%M:%S {Fore.RED}{bot.user}{Style.RESET_ALL} has connected to nextcord!"
            )
        )

class TimeSet(commands.Cog):

    def __init__(self, bot, logPath):
        self.bot = bot
        self.logPath = logPath
        self.lastUpdateTimestamp = datetime.now() # If logs are in UTC change it to datetime.utcnow()
        self.update.start()

    def splitLine(self, line: str):
        try:
            timestampStr, message = line.strip()[1:].split("]", 1)
            timestamp = datetime.strptime(timestampStr, "%d-%m-%y %H:%M:%S.%f")
            return timestamp, message
        except Exception as e:
            print(e)
            return None, None

    @tasks.loop(seconds=2)
    async def update(self):
        try:
            files = glob.glob(self.logPath +"*_DebugLog-server.txt")
            #files = glob.glob(self.logPath +"Server-console.txt")
            logging.debug(f'{Fore.GREEN}[INFO] {Style.RESET_ALL}Found {len(files)} files')
            print(f'{Fore.GREEN}[INFO] {Style.RESET_ALL}Found {len(files)} files')
            if len(files) > 0:
                with FileReadBackwards(files[len(files)-1]) as f:
                    newTimestamp = self.lastUpdateTimestamp
                    for line in f:
                        print(line)
                        logging.debug(line)
                        timestamp, message = self.splitLine(line)
                        if timestamp > newTimestamp:
                            newTimestamp = timestamp
                        if timestamp > self.lastUpdateTimestamp:
                            pattern = r"\Date in game"
                            match = re.search(pattern, message)
                            if match:
                                x = message.split('game')[1]
                                x = x.rstrip(x[-1])
                                x = x.split(' ')
                                b = self.bot.get_guild(int(GUILDID)).get_member(int(BOTID))
                                logging.debug('Changing Nickname!')
                                print('Changing Nickname!')
                                asyncio.create_task(b.edit(nick=(NAME + ' ' + x[2])))
                                break
                        else:
                            break
                    self.lastUpdateTimestamp = newTimestamp
        except Exception as x:
            logging.debug("Error ",x.args)
            print("Error ",x.args)

bot.run(TOKEN)
