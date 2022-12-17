import nextcord
import sqlalchemy as sq
from sqlalchemy.pool import QueuePool
from contextlib import contextmanager
import asyncio
import re
import requests
from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")
HOOK = os.environ.get("HOOK")

# Connect to the MySQL database
cnx = sq.create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}', pool_size=10, max_overflow=5, poolclass=QueuePool, pool_pre_ping=True)

# Get price from url
async def GetPrice(url):
    try:
        response = requests.request("GET", url)
        response =  response.content.decode('utf-8')
        x = re.findall("finalPrice.+>od (.*?) EUR</span><span data",response)
        if len(x) == 0:
            x = re.findall("finalPrice.+>(.*?) EUR</span><span data", response)
            if len(x) == 0:
                return False
        return(float(x[0].replace(",", "."))) 
    except:
        return None

@contextmanager
def get_connection():
    con = cnx.connect()
    try:
        yield con
    finally:
        con.close()

async def ccheck():
    with get_connection() as (cursor):
        result = cursor.execute("SELECT URL,PRICE FROM main").fetchall()
        if result is not None:
            for x,xx in result:
                price = await GetPrice(x)
                if price == False:
                    await Send("Item not found removing " + str(x))
                    cursor.execute("DELETE FROM main WHERE URL = %s", (x,))
                elif price == None:
                    await Send("Error with url " + str(x))
                    #cursor.execute("DELETE FROM main WHERE URL = %s", (x,))
                elif price < xx:
                    await Send("Item reached desired price " + str(x) + " is " + str(price) + " EUR")
                    cursor.execute("UPDATE main SET PRICE = %s WHERE URL = %s", (price, x))
# Send webhook
async def Send(content):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(HOOK, session=session)
        await webhook.send(content)

asyncio.run(ccheck())