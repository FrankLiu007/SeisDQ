from SeisDQ import *
from IRIS import breq_fast
from utils import event
from utils import station
from utils import event
import json
#### breq_fast request to IRIS
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
        #### add breq_fast head to pars
        pars['breq_head']=breq_head 
          
    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()
    
    reqs=breq_fast.generate_requests(pool)
    breq_fast.SendRequest(reqs)
