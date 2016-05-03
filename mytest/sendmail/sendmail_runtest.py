from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os
import io

#====================定义发送邮件===================
# def send_mail(file_latest,smtpserver, sender,username, password, receiver, subject):
#     fp = open(file_latest, 'rb')
#     mail_body = fp.read()
#     fp.close()
#
#     msg = MIMEText(mail_body, 'html', 'utf-8')
#     msg['Subject'] = Header(subject, 'utf-8')

def send_mail(smtpserver, sender,username, password, receiver, subject, sendfile):

    msg =MIMEText('<html><h1>测试报告1345</h1></html>', 'html', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')

    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;  filename="result.html"'

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out!')

#====================查找测试报告目录，找到最新生成的测试报告文件===================
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    test_dir = r'E:\seleniumTest\test_project\test_case'
    test_report = r'E:\seleniumTest\test_project\report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp =open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况：")

    runner.run(discover)
    fp.close()

    file_latest = new_report(test_report)

    smtpserver = 'smtp.sina.com'
    # 发送邮箱用户和密码
    username = 'hcr20160430@sina.com'
    password = 'hcr123456'
    # 发送邮箱
    sender = 'hcr20160430@sina.com'
    # 接收邮箱
    receiver = '839623781@qq.com'
    # receiver = 'hcr20160430@sina.com'
    #发送邮件主题
    subjcect = '自动化测试报告1213'

    #发送的附件
    sendfile = open(file_latest, 'rb').read()

    # send_mail(file_latest, smtpserver, sender, username, password, receiver, subjcect, sendfile)     #发送测试报告
    send_mail(smtpserver, sender, username, password, receiver, subjcect, sendfile)     #发送测试报告