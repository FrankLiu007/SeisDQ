#!/usr/bin/python3
#coding:utf-8
import smtplib
from email.mime.text import  MIMEText
from  email.header  import  Header
import sys
def send_email(email_par, req):

    msg=MIMEText(req, _subtype='plain')
    msg['From']=email_par["sender"]
    msg['To']=email_par["receiver"]
    msg['Subject']=Header(email_par["subject"])
    

    smtp=smtplib.SMTP()
    smtp.connect(email_par["smtpserver"])
    smtp.login(email_par["username"], email_par["password"])
    smtp.sendmail(email_par["sender"], email_par["receiver"],  msg.as_string())
    smtp.quit()
