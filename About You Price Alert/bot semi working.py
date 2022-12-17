import nextcord
import sqlalchemy as sq
from sqlalchemy.pool import QueuePool
from nextcord import Embed
from nextcord.ext import commands, menus, tasks
from contextlib import contextmanager
import asyncio
import re
import requests
from dotenv import load_dotenv
import os

load_dotenv()

async def GetPrice(url):
    response = requests.request("GET", url)
    response =  response.content.decode('utf-8')
    x = re.findall("finalPrice.+>od (.*?) EUR</span><span data",response)
    if len(x) == 0:
        x = re.findall("finalPrice.+>(.*?) EUR</span><span data", response)
        if len(x) == 0:
            return 0
    return(float(x[0].replace(",", "."))) 

TOKEN = os.environ.get("TOKEN")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")
slashperms=8
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
intents = nextcord.Intents(messages=False, guilds=True)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

bot = Bot(intents=intents)

# Connect to the MySQL database
cnx = sq.create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}', pool_size=10, max_overflow=5, poolclass=QueuePool, pool_pre_ping=True)


@contextmanager
def get_connection():
    con = cnx.connect()
    try:
        yield con
    finally:
        con.close()

@bot.event
async def on_ready():
    print("Bot is ready.")
    ccheck.start()

@tasks.loop(hours=1)
async def ccheck():
    with get_connection() as (cursor):
        result = cursor.execute("SELECT URL,PRICE FROM main").fetchall()
        if result is not None:
            for x,xx in result:
                price = await GetPrice(x)
                if price < xx:
                    await bot.get_channel(CHANNEL_ID).send("Item reached desired price " + str(x) + " is " + str(price) + " EUR")
                    cursor.execute("UPDATE main SET PRICE = %s WHERE URL = %s", (price, x))
                elif price == 0:
                    await bot.get_channel(CHANNEL_ID).send("Item " + str(x) + " is no longer available")
                    cursor.execute("DELETE FROM main WHERE URL = %s", (x,))

class MyEmbedDescriptionPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=25)

    async def format_page(self, menu, entries):
        embed = Embed(title="Stuff", description="\n".join(entries))
        embed.set_footer(text=f"Page {menu.current_page + 1}/{self.get_max_pages()}")
        return embed

@bot.slash_command(name="listx", description="Lists all mods monitored by this Guild!", default_member_permissions=slashperms)#, guild_ids = servers)
async def listx(interaction: nextcord.Interaction):
        await interaction.response.defer()
        try:
            with get_connection() as (cursor):
                data = cursor.execute(f"SELECT URL,PRICE from main").fetchall()
            leng=len(data) # Get number of mods
            t = 30
            if leng > 75: # If more than 75 mods, increase timeout for embed
                t = t * (leng / 50)
            data = [("#%s %s | %s" % (num,data[num][1],data[num][0])) for num in range(0, leng)]
            pages = menus.ButtonMenuPages(
                source=MyEmbedDescriptionPageSource(data),
                clear_buttons_after=True#,
                #timeout=t, # Timeout for embed, idk if needed but just in case
            )
            await pages.start(interaction=interaction)
        except Exception as ex:
            print(ex.args)
            await interaction.followup.send("Error")

bot.run(TOKEN)