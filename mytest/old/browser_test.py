##################################
#浏览器最大化
# #coding=utf-8
# from selenium import webdriver
# import time
#
# dr = webdriver.Firefox()
# dr.get("http://www.baidu.com")
#
# print("浏览器最大化")
#
# dr.maximize_window()      #将浏览器最大化显示
# time.sleep(3)
#
# dr.find_element_by_id("kw").send_keys("selenium")
# dr.find_element_by_id("su").click()
#
# time.sleep(5)
#
# dr.close()




#######################################
#设置浏览器宽和高
#coding=utf-8
from selenium import webdriver
import time

dr = webdriver.Firefox()
dr.get("http://m.mail.10086.cn")
time.sleep(5)

#设置数字为像素点
print("设置浏览器宽1920、高1080显示")
dr.set_window_size(1920,1080)
time.sleep(5)

dr.close()
