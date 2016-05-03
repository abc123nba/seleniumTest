#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

dr = webdriver.Firefox()
dr.get("http://www.baidu.com")

################百度输入框的定位方式#################

#通过id方式定位
dr.find_element_by_id("kw").send_keys("python")                 #find_element_by_id("kw")函数捕获到百度输入框【id】

#通过name方式定位
dr.find_element_by_name("wd").send_keys("selenium & python")  #find_element_by_name("wd")函数也可捕获百度输入框【name】

#通过tag name方式定位
# dr.find_element_by_tag_name("input").send_keys("java")             #存在多个input

#通过class name方式定位
dr.find_element_by_class_name("s_ipt").send_keys("JDK")

#通过CSS方式定位
dr.find_element_by_css_selector("#kw").send_keys("selenium + python")
# dr.find_element_by_css_selector("a[name=\"wd\"]").send_keys("C++")

#通过xphan方式定位     xpath:attributer(属性)
dr.find_element_by_xpath("//input[@id='kw']").send_keys("selenium web")    #input标签下id=kw的元素


#link定位
dr.find_element_by_link_text("贴吧").click()      #不是一个输入框也不是一个按钮，而是一个文字链接，可通过link

#partial link text定位
dr.find_element_by_partial_link_text("贴").click()   #通过find_element_by_partial_link_text()函数，只用了“贴”，脚本一样找到了“贴吧”的链接


########################################################
dr.find_element_by_id("su").click()
time.sleep(5)

dr.close()






