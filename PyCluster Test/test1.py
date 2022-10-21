from dask.distributed import Scheduler, Client
import time
import asyncio
import os
async def test():
    await asyncio.sleep(1)
    
if __name__ == '__main__':
    print('Starting cluster...')
    while True:
    #Scheduler(loop=15,port=6969)
        try:
          os.system("dask-worker localhost:8786 --nworkers 2 --nthreads 1")
        except Exception as e:
            print(e)
            print('Starting cluster...')
            time.sleep(5)
            continue
    #while True:
        #asyncio.run(test())

