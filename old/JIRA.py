#coding=utf-8
from selenium import webdriver
from time import sleep
from public_login import login
from public_logout import logout

dr = webdriver.Firefox()
url = 'http://116.211.105.54:8080/jira/secure/Dashboard.jspa'
dr.get(url)
sleep(5)

# login(dr,'houchangrun','123@abc')
# cookie1 = dr.get_cookies()
# print(cookie1)
# sleep(10)
# logout(dr)

login(dr,'zhangyu','111111')
# cookie2 = dr.get_cookies()
# print(cookie2)
sleep(10)
logout(dr)
sleep(5)

# dr.close()
