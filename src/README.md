# SeisDQ 
<b>Sei</b>smic <b>D</b>ata <b>Q</b>uery

>SeisDQ is a flexible seismic framework to fetch seismic data from online or local database.
It can be implimented easily for other purpose.
## Brief history of SeisDQ
- GetEvent.py
> When I was a graduate student, I used to process raw seismic data recorded by reftek rt130. The first step is convert all data to miniseed and then event data was cutted. I decided to write a script to directly fetch raw data from data achive (GetEvent.py).

- Breq.py
> When I started to do my research dependently, I need to request data from IRIS (Incorporated Research Institutions for Seismology). I wrote a script to apply for data through the breq_fast. 
 - splitlab
  > I write scripts to prepare data for splitlab to estimate shear wave splitting.

**Found Problem**
- [ ] The codes above are similar.
- [ ] It is difficult to maintain the code.
  
  > They all contains travel time calculation, data application, data preprocess ( convert to proper format, add header information etc.)

At last, I decided to refactor the code.

### requirements

* python of version 3 (3.6 or higher recommended), 
* TauP (version 2.4.5) or ttimes (available in ) to calculate travel time
* distaz, I provided distaz.f in directory "utils", please compile it and add it to  system PATH.
* reftek tools (arcfetch, rt_sac) if used to get data recorded by rt130 from local storage. I will delete them if ......

### installation && ussage
> download the source code
> install requirements
>  goto the test directory, and run tests:
1. breq_fast test: 
```python breq_test.py breq.head ```
2. reftek test: 
```python reftek_test.py reftek_data_dir  output_dir ```


At present, the code is only tested on linux, but should be used on windows and macos with small modifications.


### implimention
In order to impliment this code for other purpose, please refer to the reftek_test.py and iris.test.py