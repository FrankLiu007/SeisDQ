from SeisDQ import *

def Rt130Fetch(pars):
    pars=read_pars(pars_path)
    stations=read_stations(pars['stations']['path'])
    events=read_NEIC_csv_events()
    pool=SeismicPool(pars, stations, events)
    all_data=pool.process()
    RequestIris(all_data)
    SaveData()
    
    generate_()
    send2iris(all)
