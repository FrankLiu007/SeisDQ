from SeisDQ import DataPool
from IRIS.breq_fast import *
from utils import station, event
import json

if __name__ == "__main__":

    pars_path="par.json"
    breq_path="breq.head"
    with open(pars_path,'r') as f :
        pars= json.load(f)
        if not pars:
            print("error reading parameter files!")
            exit(-1)
    with open(breq_path,'r') as f :
        breq_head= json.load(f)
        if not breq_head:
            print("error reading parameter files!")
            exit(-1)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()
    
    reqs=generate_requests(pool, breq_head)
    SendRequest(reqs)