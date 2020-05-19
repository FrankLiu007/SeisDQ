import csv
import datetime
def read( path):
    stations=[]
    with open(path, 'r') as inf :
        i=0
        for station in csv.DictReader(inf):
            station['id']=i
            t0=datetime.datetime.strptime(station['start_time'],'%Y-%m-%d')
            t1=datetime.datetime.strptime(station['end_time'],'%Y-%m-%d')
            station["time_range"]=[t0, t1]
            i=i+1
            stations.append(station)
    return stations


