import json
import requests
from collections import Counter
import datetime
import sys
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("TOKEN")


def GetNFTS(policy,DAN):
    NFTS = list()
    for a in range(1,21474836):
        x = ApiCall(f'assets/policy/{policy}',{'page':a})
        if x == []:
            break
        NFTS+=x
    WriteFile('NFTs',NFTS,policy,DAN)
    return NFTS

def GetHolders(NFTS,policy,DAN):
    Holders = list()
    for a in NFTS:
        asset = a["asset"]
        x = ApiCall(f'assets/{asset}/addresses')
        Holders+=x
    WriteFile('Holders',Holders,policy,DAN)
    return Holders

def GetStake(Holders,policy,DAN):
    Stake = list()
    for a in Holders:
        asset = a["address"]
        x = ApiCall(f'addresses/{asset}')
        x = {'address':x['address'],'stake':x['stake_address']}
        Stake.append(x)
        counter = Counter(item.get('stake') for item in Stake)
    WriteFile('Stake',dict(counter.most_common()),policy,DAN)
    return dict(counter.most_common())

def WriteFile(name,x,POL,DAN):
    if not os.path.exists(POL):
        os.mkdir(POL)
    if not os.path.exists(f'{POL}/{DAN}'):
        os.mkdir(f'{POL}/{DAN}')
    with open(f'./{POL}/{DAN}/{name}.json', 'w+') as f:
        json.dump(x, f, indent=4)
    return True

def ApiCall(url, paramsx = ''):
    try:
        url = f'https://cardano-mainnet.blockfrost.io/api/v0/{url}'
        myobj = {'project_id' : TOKEN}
        resp = requests.get(url, headers = myobj, params=paramsx)
        if resp.status_code != 200:
            sys.exit(f'API returned error code for {url}')
        return resp.json()
    except:
        sys.exit(f'Fatal Error during API query :(')

def DataLen(x):
    f = open(x, 'r')
    data = json.load(f)
    return len(data)

def DataLoad(x):
    f = open(x, 'r')
    data = json.load(f)
    return data

def main():
    if len(sys.argv) == 2:
       print(GenReport(sys.argv[1]))
    elif len(sys.argv) > 2:
       print('Too many command-line arguments')
       sys.exit(1)
    else:
       print('Missing command-line argument')
       sys.exit(1)

def GenReport(policy):
    DAN = datetime.date.today()
    NFTS = GetNFTS(policy,DAN)
    HOLDERS = GetHolders(NFTS,policy,DAN)
    Stake = GetStake(HOLDERS,policy,DAN)

    rep = list()
    rep.append({'NFTS':len(NFTS),'HOLDERS':len(HOLDERS),'Stake':len(Stake)})
    WriteFile('Count',rep,policy,DAN)
    return 'Report generated!'

if __name__ == "__main__":
    main()



