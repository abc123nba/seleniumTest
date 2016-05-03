#coding=utf-8
from selenium import webdriver
import time   #调入time函数

dr = webdriver.Firefox()
dr.get("http://www.baidu.com")

# time.sleep(3)   #休眠0.3秒

dr.implicitly_wait(30)   #智能等待30秒

dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()

# time.sleep(5)   #休眠3秒

dr.close()
