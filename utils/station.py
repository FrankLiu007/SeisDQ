

def read( path):
    inf=open(path, 'r')
    stations=[]
    while True:
        str0=inf.readline()
        if str0=='':
            break
        tt=str0.split()
        if(len(tt)==0 or tt[0]=='#'):
            continue
        start_time=datetime.datetime.strptime(tt[2],'%Y-%m-%dT%H:%M:%S')
        end_time=datetime.datetime.strptime(tt[3],'%Y-%m-%dT%H:%M:%S')

        stations.append({'network':tt[0],'name':tt[1],'start_time':start_time, 'end_time':end_time,'lat':tt[4], 'lon':tt[5]})
    inf.close()
    return stations