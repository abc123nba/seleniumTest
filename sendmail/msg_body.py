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

#接收邮箱
receiver = '839623781@qq.com'
#发送邮件主题
subject = 'add result to context '

#编写HTML类型的邮件正文
with open('E:\\seleniumTest\\test_project\\report\\2016-05-01_12_13_35result.html') as fp:
    msg = MIMEText(fp.read())
# fp = open(r'E:\seleniumTest\test_project\report\2016-05-01_12_13_35result.html', 'rb')
#     mail_body = fp.read()
# fp.close()

# msg = MIMEText(mail_body, 'html', 'utf-8')

# msg = MIMEText('<html><h1>你好！邮箱密码hcr123456</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()