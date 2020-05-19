#!/usr/bin/python3


import datetime
import json
from utils import neic
from utils.TravelTime import calculate_travel_time

class DataPool:
    def __init__(self, pars, events, stations):
        self.pars=pars
        self.events=events
        self.stations=stations
        self.all_data=""

    def process(self):
        for station in self.stations:
            stnet=station['network']
            stnm=station['name']
            for event in self.events:
                b_mag, e_mag=event['magnitude_range']
                if (event_)
                if( mag<b_mag or mag>e_mag):
                    continue
                data1=processing_event(station, event, pars)
                all.append(data1)
##--------------------processing one-event  --------------------
    def processing_one_event(self, station, event, pars):
        result=dict()
        tmin=station['start_time']
        tmax=station['end_time']

        evla=event['lat']
        evlo=event['lon']
        evdep=event['depth']

        t1=event['time']

        time0=0
        time1=0
        b_phase=par['seismic_phase']['begin']['phase']
        e_phase=par['seismic_phase']['end']['phase']

        t0=calculate_travel_time(station['lat'], station['lon'], event['lat'], event['lon'], evdep, b_phase, par['travel_time_tool'])
        if(b_phase==e_phase):
        t1=t0
        else:
            t1=calculate_travel_time(station['lat'], station['lon'], event['lat'], event['lon'], evdep, e_phase, par['travel_time_tool'])

        return result

    def save(self):
        for station in self.stations:
            for event in self.events:

###read parameters       
def read_pars( path):
    with open(path,'r') as f :
        return json.load(f)
##read all stations        
    
def SaveData()
    pass


