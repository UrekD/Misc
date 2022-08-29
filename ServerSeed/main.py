import a2s
import time
import json

address = ("172.93.183.42",27135)
class Seeder:
    def __init__(self):
        self.d = {}
        try:
            self.d = json.load(open("seeders.txt"))
        except:
            pass
        
    def sstart(self):
        while True:
            try:
                m = (a2s.info(address).map_name)
                if 'seed' in m.lower():
                   break
                x = a2s.players(address)
                for i in x:
                    if i.name == "":
                        continue
                    elif i.name not in self.d:
                        self.d[i.name] = 0
                    else:
                        self.d[i.name] += 1
                print('Done')
                time.sleep(60)
            except:
                break


        self.d = dict(sorted(self.d.items(), key=lambda item: item[1], reverse=True))
        #for a in self.d:
            #print(a, self.d[a])
        print(f'Total players: {len(self.d)}')
        json.dump(self.d, open("seeders.txt",'w'))
    
x = Seeder()
x.sstart()


