#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.sina.com'
username = 'hcr20160430@sina.com'
password = 'hcr123456'
sender = 'hcr20160430@sina.com'
receiver = '839623781@qq.com'
subject = 'Add 110 result.html to mail body'

#编写HTML类型的邮件正文
with open(r'D:\test\2016-05-01_10_55_28result.html') as fp:
    msg = MIMEText(fp.read().encode("utf-8").decode('utf-8'), 'html')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()