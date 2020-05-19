import subprocess
import pexpect

def calculate_travel_time(evla, evlo,depth, stla, stlo, phases):
    if pars['travel_time_tool'].lower()=="taup":
        return travel_time_taup(evla, evlo,depth, stla, stlo, phases)
    elif pars['travel_time_tool'].lower()=="ttimes":
        dist=get_distance(evla, evlo,  stla, stlo)
        return travel_time_ttimes(phases,depth,dist)

#####    
def get_distance(evla, evlo,  stla, stlo):
    distaz='distaz '+ evla +' '+ evlo + ' '+  stla +' '+ stlo
    status, out1= subprocess.getstatusoutput(distaz)
    if(status!=0):
        print('Command ',distaz,' failed')
        return ''
    return float(out1.split()[0])

def travel_time_taup(evla, evlo,depth, stla, stlo, dist, phases):
    taup_time -mod iasp91 -h 143.2 -deg 75 -ph
    cmd="taup_time -mod iasp91 -e " + str(evla)+","+ str(evlo) + " -h "+ str(depth) \
        + " -s "+ str(stla)+","+str(stlo) +" -deg "+str(dist)  
    
    ph=''
    for phase in phases:
        ph=ph+phase+","
    cmd=cmd+ph[:-1] +  "  --json  "
    status, out1= subprocess.getstatusoutput(cmd)
    
    if(status!=0):
        print('Command ',cmd,' failed')
        return []
    results=json.loads(out1)

    out={}    
    for arr in results["arrivals"]:
        out[arr["phase"]]={ "time":arr["time"], "rayp":arr["rayparam"]}

    return out

    
def travel_time_ttimes(phases,depth,dist):

    child=pexpect.spawn("ttimes")
    child.expect_exact("*")
    for phase in phases:
        child.sendline(phase)
        child.expect_exact("*")
    child.sendline()
    child.expect_exact("Source depth (km):")
    child.sendline(str(depth))
    child.expect_exact("Enter delta:")
    child.sendline(str(dist))
    child.expect_exact("Enter delta:")    
    zz=child.before.decode().split('\r\n')
    child.close()

    out={}   
    i=1 
    for line in zz:
        if not "E-0" in line:
            continue
        kk=line[10:].split()
        out[ kk[1] ]={"rayp":kk[5], "time":kk[2]}

    return out

def send_mail(fname):
    import smtplib
    from email.mime.text import  MIMEText
    from  email.header  import  Header
    import sys

    sender='liuqimin2009@163.com'
    receiver='breq_fast@iris.washington.edu'
#    receiver='284693929@qq.com'
    subject='breq'
    smtpserver='smtp.163.com'
    username='liuqimin2009'
    password='yjynkn$1101'

    inf=open(fname,'r')
    tt=inf.read()
    msg=MIMEText(tt,_subtype='plain')
    msg['Subject']=Header(subject)
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()