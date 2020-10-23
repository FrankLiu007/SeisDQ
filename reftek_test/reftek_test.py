### append sys.path first
import sys
import argparse
sys.path.append("../src")
from SeisDQ import DataPool

from utils import station, event
from utils import common
import  reftek

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--par", help="location of the parameters file .", required=True)
    args=parser.parse_args()

    # pars_path="par.json"
    pars=common.read_json(args.par)

    stations=station.read(pars['station_path'])
    events=event.read_events(pars['events'])
    pool=DataPool(pars, stations, events)
    all_data=pool.process()
    pool.save("lg.pool")

    result=reftek.fetch_data(pool)
##examples to add headers to file
    print("begin adding event information to files")
    if pool.pars['output_data_format'].lower()=='sac':
        reftek.add_sac_head(result) 