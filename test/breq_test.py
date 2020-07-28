from SeisDQ import DataPool
from IRIS.breq_fast import *
from utils import station, event
from utils import read_json

if __name__ == "__main__":

    pars_path="par.json"
    pars=read_json.read(pars_path)

    breq_path="breq.head"
    breq_head= read_json.read(pars_path)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()
    
    reqs=generate_requests(pool, breq_head)
    SendRequest(reqs)