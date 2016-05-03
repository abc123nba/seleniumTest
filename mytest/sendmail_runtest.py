#coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os

#====================瀹氫箟鍙戦�閭�欢===================
def send_mail( file_new,smtpserver, sender,username, password, receiver, subject):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg =MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out!')

#====================鏌ユ壘娴嬭瘯鎶ュ憡鐩�綍锛屾壘鍒版渶鏂扮敓鎴愮殑娴嬭瘯鎶ュ憡鏂囦欢===================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    test_dir = r'E:\seleniumTest\test_project\test_case'
    test_report = r'E:\seleniumTest\test_project\report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp =open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title="娴嬭瘯鎶ュ憡", description="鐢ㄤ緥鎵ц�鎯呭喌锛�)

    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)

    smtpserver = 'smtp.sina.com'
    # 鍙戦�閭��鐢ㄦ埛鍜屽瘑鐮�
    username = 'hcr20160430@sina.com'
    password = 'hcr123456'
    # 鍙戦�閭��
    sender = 'hcr20160430@sina.com'
    # 鎺ユ敹閭��
    # receiver = '839623781@qq.com'
    receiver = 'hcr20160430@sina.com'
    #鍙戦�閭�欢涓婚�
    subjcect = '鑷�姩鍖栨祴璇曟姤鍛�

    send_mail(new_report, smtpserver, sender, username, password, receiver, subjcect)     #鍙戦�娴嬭瘯鎶ュ憡