import json
import datetime
def read_json(path):
    tt=[]
    with open(path,'r') as f :
        for line in f.readlines():
            p=line.find("#")
            if p!=-1:
                tt.append(line[:p])
            else:
                tt.append(line)
        return json.loads(''.join(tt))
    print("error reading file:"+ path)
    exit(-1)

def read_pars(path):
    pars=read_json(path)
    if pars['events']['time_range'][0]:
        pars['events']['time_range'][0]=datetime.datetime.strptime( pars['events']['time_range'][0], "%Y-%m-%d")
    else:
        pars['events']['time_range'][0]=''
    if pars['events']['time_range'][1]:   
        pars['events']['time_range'][1]=datetime.datetime.strptime( pars['events']['time_range'][1], "%Y-%m-%d")
    else:
        pars['events']['time_range'][1]=datetime.datetime.now
    return pars
