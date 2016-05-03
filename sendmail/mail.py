#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.sina.com'
username = 'hcr20160430@sina.com'
password = 'hcr123456'
sender = 'hcr20160430@sina.com'
receiver = '839623781@qq.com'
subject = 'Add myresult html to mail body'

#编写HTML类型的邮件正文
# with open(r'D:\work\seleniumTest\testallHTML\report\2016-05-03 11_01_10result.html', encoding='UTF-8') as fp:
#     msg = MIMEText(fp.read(), 'html')

with open(r'D:\test\2017.html', encoding='UTF-8') as fp:
    msg = MIMEText(fp.read(), 'html')

# with open(r'D:\test\hongten.txt', encoding='UTF-8') as fp:
#     msg = MIMEText(fp.read())

msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()