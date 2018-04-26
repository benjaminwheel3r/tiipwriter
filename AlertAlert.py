# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:34:55 2016
@author: Ben
"""
#enable https://www.google.com/settings/security/lesssecureapps
def AlertAlert(body,header,toaddr,fromaddr):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    fromaddr = "user@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = hdr
     
    body = "restart me"
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()