#coding=utf-8
from selenium import webdriver
import time

dr = webdriver.Firefox()

#访问百度首页
first_url = "http://www.baidu.com"

print("now access %s" %(first_url))
dr.get(first_url)
time.sleep(5)

#访问新闻页面
second_url = "http://news.baidu.com"
print("now access %s" %(second_url))
dr.get(second_url)
time.sleep(5)

#返回（后退）到百度首页
print("back to %s" %(first_url))
dr.back()
time.sleep(3)


#前进到新闻页面
print("forward to %s" %(second_url))
dr.forward()
time.sleep(3)

dr.close()