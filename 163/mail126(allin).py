#coding=utf-8
from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.implicitly_wait(10)
url = 'http://mail.163.com/'
dr.get(url)

#登录
dr.find_element_by_id('idInput').send_keys('hcr258')
dr.find_element_by_id('pwdInput').send_keys('hcr20160422')
dr.implicitly_wait(10)

dr.find_element_by_id('loginBtn').click()
sleep(10)

dr.find_element_by_link_text(u'退出').click()

sleep(10)

dr.close()
