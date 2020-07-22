
from SeisDQ import DataPool
from utils import station, event
from utils import read_json
from reftek import fetch  

if __name__ == "__main__":

    pars_path="par.json"
    pars=read_json.read(pars_path)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()
    fetch(pool)
