import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.sina.com'
username = 'hcr20160430@sina.com'
password = 'hcr123456'
sender = 'hcr20160430@sina.com'
receiver = '839623781@qq.com'
subject = 'Python email test'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！邮箱密码hcr123456</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

