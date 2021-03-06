from SeisDQ import *
from utils import event, station
import random, string
#### breq_fast request to IRIS
import datetime

def generate_breq_requests(pool, breq):
    requests={}

    breq_head=breq["head"]
    if breq['prefix']=="begin_phase":
        prefix=pool.pars["phases"]['begin']["phase"]
    elif breq['prefix']=="end_phase":
        prefix=pool.pars["phases"]['end']["phase"] 
    prefix=prefix+'-'+''.join(random.choices('0123456789', k=4) )


    for sId, eId in pool.all_data:
        station=pool.stations[sId]
        event=pool.events[eId]

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
                breq_head['.LABEL']=stnet+"."+stnm+"-"+ prefix
                head=generate_breq_head(breq_head)
                requests[sId]=head+"\n"+tmp
        elif pool.pars["data_apply_mode"]=="per_event":
            if eId in requests:
                requests[eId]=requests[eId]+"\n"+tmp
            else:
                breq_head['.LABEL']="eventId-"+str(eId)+  prefix
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
