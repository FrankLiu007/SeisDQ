import json
def read(path):
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