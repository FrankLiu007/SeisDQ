from SeisDQ import *
from utils import event, station

import json
#### breq_fast request to IRIS
import datetime

def generate_requests(pool, breq_head):
    requests={}

    for eId, event in pool.events.items():
        for sId, station in pool.stations.items():
            if not (sId, eId) in pool.all_data:
                continue
            stnet=station["network"]
            stnm=station["name"]
            cmps=station["components"]
            loca=station["location_code"]
            t0=pool.all_data[(sId, eId)]["time_range"][0].strftime('%Y %m %d %H %M %S.%f')
            t1=pool.all_data[(sId, eId)]["time_range"][1].strftime('%Y %m %d %H %M %S.%f')

            tmp=stnet +"  "+ stnm +"  "+ t0 +" "+t1 +" " + cmps+ " "+loca
            if pool.pars["data_apply_mode"]=="per_station":                
                if sId in requests:
                    requests[sId]=requests[sId]+"\n"+ tmp
                else:
                    breq_head['.LABEL']=stnet+"."+stnm+"-"+str(sId)
                    head=generate_breq_head(breq_head)
                    requests[sId]=head+"\n"+tmp
            elif pool.pars["data_apply_mode"]=="per_event":
                if eId in requests:
                    requests[eId]=requests[eId]+"\n"+tmp
                else:
                    breq_head['.LABEL']="eventId-"+str(eId)
                    head=generate_breq_head(breq_head)
                    requests[eId]=head+"\n"+tmp
   
    return requests
def generate_breq_head(breq_head):
    breq=""
    for key, value in breq_head.items():
        if value=="":
            continue
        if breq: 
            breq=breq+"\n"+ key+" "+ value
        else: ###第一个key，不要换行
            breq= key+" "+ value
    breq=breq+"\n.END"
    return breq


def SendRequest(breqs, head, data_apply_mode):  ###not completed
    for key, req in breqs.items():
        if True:
            pass

    return 'success'

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
