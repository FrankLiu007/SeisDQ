from SeisDQ import *
from utils import event
from utils import station
from utils import event
import json
import os
#### breq_fast request to IRIS

def fetch(pool):
    requests={}
    breq=""
    out_path=""
    in_path=""
    tasks=[]
    for eId, event in pool.events.items():
        for sId, station in pool.stations.items():
            if not (sId, eId) in pool.all_data:
                continue
            stnet=station["network"]
            stnm=station["name"]
            cmps=station["components"]
            loca=station["location_code"]
            t0=pool.all_data[(sId, eId)]["time_range"][0].strftime('%Y:%j:%d:%H:%M:%S.%f')
            t1=pool.all_data[(sId, eId)]["time_range"][1].strftime('%Y:%j:%d:%H:%M:%S.%f')

            if pool.pars["data_apply_mode"]=="per_station":
                if not os.path.exists(os.path.join(out_path,stnm)):
                    os.mkdir(os.path.join(out_path,stnm))
                os.system("arcfectch "+os.path.join(in_path, stnm)+ " -C *,*,*,"+t0+","+t1+ " lqm.rt")
                os.system("rt_sac lqm.rt "+ os.path.join(out_path,stnm) )
                
            elif pool.pars["data_apply_mode"]=="per_event":
                if not os.path.exists(os.path.join(out_path, str(eId) )):
                    os.mkdir(os.path.join(out_path, str(eId)))
                os.system("arcfectch "+os.path.join(in_path, stnm)+ " -C *,*,*,"+t0+","+t1+ " lqm.rt")
                os.system("rt_sac lqm.rt "+ os.path.join(out_path, str(eId) ) ) 
    return "success"


if __name__ == "__main__":
    pars_path="par.json"
    pars=read_json.read(pars_path)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()

    fetch(pool)

