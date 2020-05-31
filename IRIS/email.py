#!/usr/bin/python3
#coding:utf-8
import smtplib
from email.mime.text import  MIMEText
from  email.header  import  Header
import sys
def send_email(sender, receiver, subject, smtpserver, username, password, reqs):
    sender='breq_fast0@163.com'
    receiver='breq_fast@iris.washington.edu'
    #receiver='284693929@qq.com'
    subject='breq申请'
    smtpserver='smtp.163.com'
    username='breq_fast0'
    password='HHKFXGMLJEDLTVUO'

    inf=open(sys.argv[1],'r')
    tt=inf.read()
    msg=MIMEText(tt,_subtype='plain')
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']=Header(subject)


    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
