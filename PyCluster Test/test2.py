import os
import httpx
import asyncio
import time

print(f"I have {os.cpu_count()} logical cores, counting hyperthreading.")

from dask.distributed import Client
if __name__ == '__main__':
    client = Client(timeout=30,address='127.0.0.1:8786')
    #client.get_versions(check=False)
    client
    

def square(x):
        return x ** 2

def neg(x):
        return -x

def test(a,b):
    return a+b*645

async def CheckOne(i):
    url = 'https://httpbin.org/get'
    #url = 'https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/'
    #myobj = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'itemcount' : 1, 'publishedfileids[0]':i}
    async with httpx.AsyncClient() as r:
        #wdetails = await r.post(url, data = myobj)
        wdetails = await r.get(url)
        return wdetails.json()['origin']
while True:
    total = client.submit(CheckOne, 1523)
    print(total.result())
    time.sleep(1)