#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

dr = webdriver.Firefox()
dr.get("http://mail.163.com/")
time.sleep(5)
dr.maximize_window()

dr.find_element_by_id("idPlaceholder").clear()
dr.find_element_by_id("idPlaceholder").send_keys("hcr258")

dr.find_element_by_id("idPlaceholder").send_keys(Keys.TAB)
time.sleep(5)
dr.find_element_by_id("pwdInput").send_keys("abc258it")

dr.find_element_by_id("pwdInput").send_keys(Keys.ENTER)

'''
dr.find_element_by_id("loginBtn").send_keys(Keys.ENTER)
'''
time.sleep(5)
dr.close()