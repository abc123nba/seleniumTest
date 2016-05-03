# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

dr = webdriver.Firefox()

dr.get("http://www.baidu.com")

#输入框输入内容
dr.find_element_by_id("kw").send_keys("selenium")
time.sleep(5)

#ctrl+a全选输入内容
dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(5)

#ctrl+x剪切输入框内容
dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(5)

#输入框重新输入内容，搜索
dr.find_element_by_id("kw").send_keys(u"虫师 cnblogs")
#dr.find_element_by_id("kw").send_keys("虫师 cnblogs")
dr.find_element_by_id("su").click()

time.sleep(5)
dr.close()








