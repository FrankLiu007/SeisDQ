import subprocess
import os
import sys
import pexpect

from SeisDQ import *
from utils import station, event, common


#### breq_fast request to IRIS
###make the data directory has achive.sta
def check_dir():
    pass


def fetch_data(pool):
    breq = ""
    result = []
    in_dir = pool.pars['input_dir']
    out_dir = pool.pars['output_dir']
    out_format = pool.pars['output_data_format']

    for sId, eId in pool.all_data:
        station = pool.stations[sId]
        event = pool.events[eId]
        rr = {}

        stnet = station["network"].strip()
        stnm = station["name"].strip()
        cmps = station["components"]
        loca = station["location_code"]
        t0 = pool.all_data[(sId, eId)]["time_range"][0].strftime('%Y:%j:%H:%M:%S.%f')
        t1 = pool.all_data[(sId, eId)]["time_range"][1].strftime('%Y:%j:%H:%M:%S.%f')

        if pool.pars["data_apply_mode"] == "per_station":
            if not os.path.exists(os.path.join(out_dir, stnet, stnm)):
                x = os.makedirs(os.path.join(out_dir, stnet, stnm))
            out_path = os.path.join(out_dir, stnet, stnm)
        elif pool.pars["data_apply_mode"] == "per_event":
            if not os.path.exists(os.path.join(out_dir, str(eId))):
                os.makedirs(os.path.join(out_dir, str(eId)))
            out_path = os.path.join(out_dir, 'event' + str(eId))
        cmd = "arcfetch " + os.path.join(in_dir, stnet, stnm) + " -C *,*,*," + t0 + "," + t1 + " lqm.rt"

        status, output = subprocess.getstatusoutput(cmd)
        if "No archive error" in output:
            print(cmd)
            print(output)
            print("Please check the data archive have the right archive.sta file. ")
            print('If not, use commond "arcrebuild -Ypass " to rebuild it.')
            exit(1)

        if not os.path.exists("lqm.rt"):
            continue

        if out_format.lower().strip() == "sac":
            cmd = "pas2sac lqm.rt " + out_path
            status, output = subprocess.getstatusoutput(cmd)

        elif out_format.lower() == "asc":
            os.system("pas2asc lqm.rt " + out_path)
        elif out_format.lower() == "msd":
            os.system("pas2msd lqm.rt " + out_path)
        elif out_format.lower() == "segy":
            os.system("pas2segy lqm.rt " + out_path)

        os.remove("lqm.rt")
        ####
        rr['event'] = event
        rr['time'] = pool.all_data[(sId, eId)]["time_range"][0]
        rr['path'] = out_path
        result.append(rr)
    return result


def add_sac_head(data):
    sac = pexpect.spawn('sac')
    for item in data:
        sac.expect("SAC>")
        str0 = "read " + item["path"] + "/" + item["time"].strftime("%Y%j%H%M%S") + "*"
        sac.sendline(str0)

        sac.expect("SAC>")
        str0 = "ch " + " evla " + str(item['event']["latitude"]) + \
               " evlo " + str(item['event']["longitude"]) + \
               " evdp " + str(item['event']["depth"])
        sac.sendline(str0)

        sac.expect("SAC>")
        sac.sendline("wh")

    sac.expect("SAC>")
    sac.sendline("q")

    return 0
