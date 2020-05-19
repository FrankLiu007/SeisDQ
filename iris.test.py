from IRIS import breq_fast
def Fetch(pars_path):
    pars=read_pars(pars_path)
    stations=read_stations(pars['stations']['path'])
    events=read_events(pars['events'])
    pool=SeismicPool(pars, stations, events)
    all_data=pool.process()

    breq_fast.SendRequest(all_data)
    pool.save()


if __name__ == "__main__":
    Fetch("par.json")