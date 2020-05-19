from SeisDQ import *
from IRIS import breq_fast
from utils import event
from utils import station
from utils import event
def Fetch(pars_path):
    pars=read_pars(pars_path)
    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()

    breq_fast.SendRequest(all_data)
    pool.save()


if __name__ == "__main__":
    Fetch("par.json")