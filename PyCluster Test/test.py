from dask.distributed import Scheduler, Client
import time
import asyncio
import os
async def test():
    await asyncio.sleep(1)
    
if __name__ == '__main__':
    print('Starting cluster...')
    #Scheduler(loop=15,port=6969)
    os.system("dask-scheduler --port 6969")
    #while True:
        #asyncio.run(test())

