######################################################
#鼠标点击 click()
#键盘输入 send_keys()
# #coding=utf-8
# from selenium import webdriver
# import time
#
# dr = webdriver.Firefox()
# dr.get("http://www.baidu.com")
#
# dr.find_element_by_id("kw").clear()
# dr.find_element_by_id("kw").send_keys("selenium")
# time.sleep(5)
#
# #通过click()来操作
# dr.find_element_by_id("su").click()
#
# time.sleep(5)
#
# dr.close()




#################################################
#提交表单 submit()
# #coding=utf-8
# from selenium import webdriver
# import time
#
# dr = webdriver.Firefox()
# dr.get("http://www.baidu.com")
#
# dr.find_element_by_id("kw").clear()
# dr.find_element_by_id("kw").send_keys("selenium")
# time.sleep(5)
#
# #通过submit()来操作
# dr.find_element_by_id("su").submit()
#
# time.sleep(5)
#
# dr.close()






################################################
#text获取元素文本
#coding=utf-8
from selenium import webdriver
import time

dr = webdriver.Firefox()
dr.get("http://www.baidu.com")
time.sleep(5)

#id = cp  元素的文本信息
data = dr.find_element_by_id("cp").text
print(data)        #打印信息
time.sleep(5)

dr.close()