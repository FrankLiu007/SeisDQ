### append sys.path first
import sys
import argparse
sys.path.append('..')

from SeisDQ import DataPool
from utils import station, event
from utils import read_json
from reftek import fetch, add_sac_head


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--par", help="location of the parameters file .")
    args=parser.parse_args()

    # pars_path="par.json"
    pars=read_json.read(args.par)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()


    result=fetch(pool)
##examples to add headers to file 
    add_sac_head(result)   