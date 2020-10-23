### append sys.path first
import sys
sys.path.append('../src')
from utils import email

from SeisDQ import DataPool
import  IRIS
from utils import station, event
from  utils import common
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--par", help="location of the parameters file .", required=True)
    parser.add_argument("--breq_head", help="breqfast head file .", required=True)
    parser.add_argument("--email_par", help="email settings used by the email utils ", required=False)
    args=parser.parse_args()

    pars=common.read_pars(args.par)

    breq_head= common.read_json(args.breq_head)

    stations=station.read(pars['station_path'])

    events=event.read_events(pars['events'])

    pool=DataPool(pars, stations, events)
    
    print("Begin calculating all travel time")
    all_data=pool.process()
## save the DataPool object  for
    print("saving data pool to local disk")
    pool.save("iris_test.pool")

    print("Generating breq fast request......")
    reqs=IRIS.generate_breq_requests(pool, breq_head)
    print("Sending breq fast request......")
    if args.email_par:
        email_par=common.read_json(args.email_par)
        for key, value in reqs.items():
            email.send_email(args.email_par, value )

    else:
        for key, value in reqs.items():
            print(key)
            print(value)
            


