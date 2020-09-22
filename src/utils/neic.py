import urllib.request
from io import StringIO
import csv
import datetime
import sys
#----------read neic events----------------------
def request_events(evt):
    ###using csv format
    neic_url="https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv"
    
    if not evt["time_range"][0]:
        print("event start time must specified!")
        sys.exit(-1)
    start_time="&starttime=" + evt['time_range'][0]
    end_time= "&endtime=" + evt['time_range'][1]
    minmagnitude= "&minmagnitude="+ str(evt['magnitude_range'][0])
    maxmagnitude= "&maxmagnitude="+ str(evt['magnitude_range'][1])
    mindepth="&maxdepth="+ str(evt['depth_range'][0])
    maxdepth="&maxdepth="+ str(evt['depth_range'][1])
    print(neic_url+start_time+end_time+minmagnitude+maxmagnitude+minmagnitude+maxmagnitude)
    res=urllib.request.urlopen(neic_url+start_time+end_time+minmagnitude+maxmagnitude+minmagnitude+maxmagnitude)
    str0=res.read().decode('utf-8')

    return read_csv_events(StringIO(str0))

def read_csv_events( inf):
    events={}
    i=0
    for evt in csv.DictReader(inf):
        evt['id']=i
        evt['time']=datetime.datetime.strptime(evt['time'],'%Y-%m-%dT%H:%M:%S.%fZ')
        evt['magnitude']=float( evt.pop('mag') )
        evt['depth']= float(evt['depth'])
        evt['latitude']=float(evt['latitude'])
        evt['longitude'] =float (evt['longitude'])
        events[i]=evt
        i=i+1
    return events

def main():
    evt= {
        "path":"",  ###leave blank if you want to download event from neic
        "depth_range":[0, 6371 ], 
        "magnitude_range":[5,9.9],
        "time_range":["2014-01-01","2014-01-02"],

    }
    events=request_events(evt)
    for event in events:
        print(events['event'])

if __name__ == "__main__":
    main()