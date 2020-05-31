'''
    events format:
    {
        "path":"",  ## if blank, events will be downlaoded from neic
        "depth_range":[0, 6371 ], 
        "magnitude_range":[0,9.9],
        "time_range":["2010-01-01","2010-01-02"]
    }
'''
from . import neic
def filter_events(events, evt):
    result={}
    for id, event in events.items():
        if event['magnitude']>evt['magnitude_range'][1]  or event['magnitude']<evt['magnitude_range'][0]:
            continue
        if event['time']>evt['time_range'][1]  or event['time']<evt['time_range'][0]:
            continue
        if event['depth']>evt['depth_range'][1]  or event['depth']<evt['depth_range'][0]:
            continue
        result[id]=event
    return result

def read_events(evt):
    events=[]
    if evt['path']!='':
        print("event['path'] not set, begin request event from NEIC")
        with open(evt['path']) as f :
            inf=StringIO(f.read())
            events=neic.read_csv_events(inf)
            events=filter_events(events)
        if not events:
            print("failed reading events from local file!")
            print("start getting events from NEIC through http")
            events=neic.request_events(evt)
    else:
        events=neic.request_events(evt)

    return events