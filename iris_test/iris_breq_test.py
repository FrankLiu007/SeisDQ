### append sys.path first
import sys
sys.path.append('..')

from SeisDQ import DataPool
from IRIS.breq_fast import *
from utils import station, event
from  utils import common

if __name__ == "__main__":

    pars_path="par.json"
    pars=common.read_pars(pars_path)

    breq_path="breq.head"
    breq_head= common.read_json(breq_path)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()
    
    reqs=generate_requests(pool, breq_head)
    SendRequests(reqs)

## save the DataPool object  for 
    pool.save("iris_test.pool")