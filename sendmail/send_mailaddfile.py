import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#sina邮箱
#发送邮件服务器
smtpserver = 'smtp.sina.com'
#发送邮箱用户和密码
username = 'hcr20160430@sina.com'
password = 'hcr123456'
#发送邮箱
sender = 'hcr20160430@sina.com'

#接收邮箱
receiver = '839623781@qq.com'

#发送邮件主题
subject = 'Python send email test(add file)'

#发送的附件
sendfile = open(r'D:\tools\DnsJumper v1.0.4\Readme.txt', 'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;  filename="Readme.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()