###################################
#打印页面title
# #coding=utf-8
# from selenium import webdriver
#
# dr = webdriver.Firefox()
#
# dr.get("http://www.baidu.com")
# print(dr.title)     #把页面title打印出来
#
# dr.close()
#


#coding=utf-8
from selenium import webdriver
import time

dr = webdriver.Firefox()
url = "http://www.baidu.com"

#通过get方法获取当前的URL打印
print("now access %s" %(url))
dr.get(url)
time.sleep(5)

dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
time.sleep(5)

dr.close()