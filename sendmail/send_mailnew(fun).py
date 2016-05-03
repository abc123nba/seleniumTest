#coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os

#====================定义发送邮件===================
# def send_mail(file_new):
    # f = open(file_new, 'rb')
    # mail_body = f.read()
    # f.close()

def send_mail(smtpserver, username, password, sender, receiver, subject) :
    msg =MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out!')

if __name__ == '__main__':

    # test_dir = r'E:\seleniumTest\test_project\test_case'
    # test_report = r'E:\seleniumTest\test_project\report'

    smtpserver = 'smtp.sina.com'
    # 发送邮箱用户和密码
    username = 'hcr20160430@sina.com'
    password = 'hcr123456'
    # 发送邮箱
    sender = 'hcr20160430@sina.com'
    # 接收邮箱
    receiver = '839623781@qq.com'
    # receiver = 'hcr20160430@sina.com'
    # 发送邮件主题
    subject = '自动化测试报告1203'

    send_mail(smtpserver, username, password, sender, receiver, subject)     #发送测试报告