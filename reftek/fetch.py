import subprocess
import os
import sys
import pexpect


from SeisDQ import *
from utils import station, event, read_json
#### breq_fast request to IRIS

def fetch(pool):
    breq=""
    result=[]
    in_dir=pool.pars['input_dir']
    out_dir=pool.pars['output_dir']
    out_format=pool.pars['output_data_format']

    for eId, event in pool.events.items():
        for sId, station in pool.stations.items():
            rr={}
            if not (sId, eId) in pool.all_data:
                continue
            stnet=station["network"]
            stnm=station["name"]
            cmps=station["components"]
            loca=station["location_code"]
            t0=pool.all_data[(sId, eId)]["time_range"][0].strftime('%Y:%j:%d:%H:%M:%S.%f')
            t1=pool.all_data[(sId, eId)]["time_range"][1].strftime('%Y:%j:%d:%H:%M:%S.%f')

            if pool.pars["data_apply_mode"]=="per_station":
                if not os.path.exists(os.path.join(out_dir,stnet, stnm)):
                    x=os.mkdir(os.path.join(out_dir,stnm))
                out_path=os.path.join(out_dir, stnet, stnm)
            elif pool.pars["data_apply_mode"]=="per_event":
                if not os.path.exists(os.path.join(out_dir, str(eId) )):
                    os.mkdir(os.path.join(out_dir, str(eId)))
                out_path=os.path.join(out_dir, 'event'+str(eId) ) 

            status, output=subprocess.getstatusoutput("arcfectch "+os.path.join(in_dir, stnm)+ " -C *,*,*,"+t0+","+t1+ " lqm.rt")
            
            
            if out_format.lower()=="sac":
                os.system("pas2sac lqm.rt "+ out_path )

            elif out_format.lower()=="asc":
                os.system("pas2asc lqm.rt "+ out_path )
            elif out_format.lower()=="msd":
                os.system("pas2msd lqm.rt "+ out_path )
            elif out_format.lower()=="segy":
                os.system("pas2segy lqm.rt "+ out_path )
            ####
            rr['event']=event
            rr['time']=pool.all_data[(sId, eId)]["time_range"][0]
            rr['path']=out_path
            result.append(rr)
    return result

def add_sac_head(data):
    sac=pexpect.spawn('sac')
    for item in data:
        sac.expect("SAC>")
        str0="read "+ item["path"]+"/"+item["time"].strftime()+ "*"
        sac.sendline(str0)

        sac.expect("SAC>")
        str0="ch "+ " evla "+ item['event']["latitude"] + \
        " evlo "+ item['event']["longitude"]+ \
            " evdp "+ item['event']["depth"]
        sac.sendline(str0)

        sac.expect("SAC>")
        sac.sendline("wh")

    sac.expect("SAC>")
    sac.sendline("q")

    return 0




if __name__ == "__main__":
    pars_path="../test/par.json"
    pars=read_json.read(pars_path)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()

    in_dir=sys.argv[1]
    out_dir=sys.argv[2]
    out_format=sys.argv[3]
    result=fetch(pool, in_dir, out_dir, out_format)
##examples to add headers to file 
    add_sac_head(result)   
