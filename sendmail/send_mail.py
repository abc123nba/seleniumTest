import smtplib
from email.mime.text import MIMEText
from email.header import Header

#sina邮箱
#发送邮件服务器
smtpserver = 'smtp.sina.com'
#发送邮箱用户和密码
username = 'hcr20160430@sina.com'
password = 'hcr123456'
#发送邮箱
sender = 'hcr20160430@sina.com'


# #163邮箱
# #发送邮件服务器
# smtpserver = 'smtp.163.com'
# #发送邮箱用户和密码
# username = 'hcr258@163.com'
# password = 'hcr20160422'
# #发送邮箱
# sender = 'hcr258@163.com'


#接收邮箱
receiver = '839623781@qq.com'

#发送邮件主题
subject = 'Python email test'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！邮箱密码hcr123456</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

######################
"""
邮件服务器需开启SMTP服务
smtp.sina.com
"""
######################