c     main program
c
c     XY, 11.2002
c
      real slat,slon,elat,elon,dist,az,baz
      character*20 name

      narg=iargc()
      if (narg.eq.0) then
         write(*,91)
         write(*,92)
         read(*,*) slat,slon
         write(*,93)
         read(*,*) elat,elon
      else if (narg.gt.0) then
         call getarg(1,name)
         if (name(1:2).eq.'-h'.or.name(1:2).eq.'-H') then
            write(*,91)
            write(*,94)
            write(*,95)
            stop
         else
            call getarg(1,name)
            read(name,*) slat
            call getarg(2,name)
            read(name,*) slon
            call getarg(3,name)
            read(name,*) elat
            call getarg(4,name)
            read(name,*) elon
         endif
      endif

      call distaz(slat,slon,elat,elon,dist,az,baz)
      write(*,*) dist,baz,az

   91 format('distaz --- calculates distance,azimuth and back-azimuth'
     &,' between two geographic points.')
   92 format('Input latitude and longitude of point one: ',$)
   93 format('Input latitude and longitude of point two: ',$)
   94 format('Usage: distaz [lat1,lon1,lat2,lon2]')
   95 format('Output: dist baz az.')
      stop
      end


	subroutine distaz (stnp,stnl,ep,el,angi,az,baz)
c
c   Computation of distance,azimuth and back-azimuth between
c   two point of the earth
c
c   from Winfried Hanka, 11.2002
c
       arcos(xxx) = atan(sqrt(1.0-xxx*xxx)/xxx)
       pi = 3.1415927
       rad = 0.01745329
       esqi = 0.9932315
       epipr = ep*rad
       epipr = 90.*rad-atan(esqi*(sin(epipr)/cos(epipr)))
       epipc = epipr/rad
       if(el) 200,201,201
200    epilc = 360.+el
       go to 202
201    epilc = el
202    epilr = epilc*rad
       if(abs(stnp)-90.) 111,112,112
112    angi = 90.+ep
       az = 180.
       baz = 0.
       go to 998
111    stpc = stnp*rad
       stnpr = 90.*rad-atan(esqi*(sin(stpc)/cos(stpc)))
       stpc = stnpr/rad
       if(stnl) 211,212,212
211    stlc = 360.+stnl
       go to 213
212    stlc = stnl
213    if(stpc-180.) 69,68,68
68     angi = 180.-epipc
       az = 180.
       baz = 0.
       go to 998
69     stnlr = stlc*rad
c
c******************
c
c      determine polar angle
       pang = abs(stlc-epilc)
       if(pang-180.) 71,71,70
70     pang = 360. -pang
71     pang = pang*rad
       angi = cos(epipr)*cos(stnpr)+sin(epipr)*sin(stnpr)*cos(pang)
       angi = arcos(angi)
       if(angi) 220,221,221
220    angi = angi+pi
221    az = (cos(stnpr)-cos(epipr)*cos(angi))/(sin(epipr)*sin(angi))
       az = arcos(az)
       if(az) 230,231,231
230    az = az+pi
231    az = az*57.295780
       baz = (cos(epipr)-cos(stnpr)*cos(angi))/(sin(stnpr)*sin(angi))
       baz = arcos(baz)
       if(baz) 240,241,241
240    baz = baz+pi
241    baz = baz*57.295780
       angi = angi*57.295780
       if(stlc-epilc) 72,74,73
72     if(stlc-epilc+180.) 80,77,81
73     if(stlc-epilc-180.) 80,77,81
74     if(stpc-epipc) 75,78,76
75     az = 0.
       baz = 180.
       go to 998
76     az = 180.
       baz = 0.
       go to 998
77     if(stpc+epipc-180.) 78,78,79
78     az = 0.
       baz = 0.
       go to 998
79     az = 180.
       baz = 180.
       go to 998
80     baz = 360. - baz
       go to 998
81     az = 360.-az
998    return
       end
