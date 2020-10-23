import subprocess
import pexpect
import sys
import json
def calculate_travel_time(dist, evdep, phases, tool):
    if tool.lower()=="taup":
        return travel_time_taup(dist, evdep,  phases)
    elif tool.lower()=="ttimes":
        return travel_time_ttimes(phases,evdep,dist)

#####    
def get_distance(evla, evlo,  stla, stlo):
    distaz='distaz '+ str(evla) +' '+  str(evlo) + ' '+  str(stla) +' '+ str(stlo)
    status, out1= subprocess.getstatusoutput(distaz)
    if(status!=0):
        print('Command ',distaz,' failed')
        return ''
    return float(out1.split()[0])

def travel_time_taup(dist,depth,   phases):
    cmd="taup_time -mod iasp91 -deg " + str(dist)+ "  -h "+ str(depth)  
    ph=' -ph '
    for phase in phases:
        ph=ph+phase+","
    cmd=cmd+ph[:-1] +  "  --json  "
    status, out1= subprocess.getstatusoutput(cmd)
    
    if(status!=0):
        print('Command ',cmd,' failed')
        sys.exit(-1)
    results=json.loads(out1)
    out={}    
    for arr in results["arrivals"]:
        out[arr["phase"]]={ "time":float(arr["time"]), "rayp":float(arr["rayparam"])}

    return out

    
def travel_time_ttimes(phases,depth,dist):

    child=pexpect.spawn("ttimes")
    child.expect_exact("*")
    for phase in phases:
        child.sendline(phase)
        child.expect_exact("*")
    child.sendline()
    child.expect_exact("Source depth (km):")
    child.sendline(str(depth))
    child.expect_exact("Enter delta:")
    child.sendline(str(dist))
    child.expect_exact("Enter delta:")    
    zz=child.before.decode().split('\r\n')
    child.close()

    out={}   
    i=1 
    for line in zz:
        if not "E-0" in line:
            continue
        kk=line[10:].split()
        out[ kk[1] ]={"rayp":float(kk[5]), "time":float(kk[2]) }

    return out
