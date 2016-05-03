#coding=utf-8
from time import sleep

import model
from selenium import webdriver

dr = webdriver.Firefox()
dr.implicitly_wait(10)
url = 'http://mail.163.com'
dr.get(url)

#调用登录模块
model.login(dr)

sleep(10)

#调用退出模块
model.logout(dr)

sleep(5)

dr.close()
