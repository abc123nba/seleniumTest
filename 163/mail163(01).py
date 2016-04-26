#coding=utf-8
from selenium import webdriver
from time import sleep

#登录
def login():
    dr.find_element_by_id('idInput').clear()
    dr.find_element_by_id('idInput').send_keys('hcr258')
    dr.find_element_by_id('pwdInput').clear()
    dr.find_element_by_id('pwdInput').send_keys('hcr20160422')
    dr.find_element_by_id('loginBtn').click()

#退出
def logout():
    dr.find_element_by_link_text(u'退出').click()

dr = webdriver.Firefox()
dr.implicitly_wait(10)
url = 'http://mail.163.com'
dr.get(url)

login()  #调用登录模块
sleep(10)

logout()  #调用退出模块
sleep(5)

dr.close()