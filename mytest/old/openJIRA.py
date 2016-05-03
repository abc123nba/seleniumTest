#coding=utf-8
from selenium import webdriver
from time import sleep

# dr = webdriver.Firefox()
dr = webdriver.Chrome()
dr.get('http://116.211.105.54:8080/jira/secure/Dashboard.jspa')

dr.find_element_by_id('login-form-username').clear()
dr.find_element_by_id('login-form-username').send_keys('houchangrun')
sleep(5)
dr.find_element_by_id('login-form-password').clear()
dr.find_element_by_id('login-form-password').send_keys('123@abc')

dr.find_element_by_id('login-form-remember-me').click()
dr.find_element_by_id('login').submit()

sleep(5)

# dr.close()
