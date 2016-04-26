#coding=utf-8
from selenium import webdriver     # 要使用selenium的webdriver函数，先要把包导进来

browser = webdriver.Firefox()       #要操控firefox浏览器
browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("selenium")    #输入框的id叫kw，要在输入框里输入selenium
browser.find_element_by_id("su").click()                    #搜索的按钮的id叫su，需要点一下按钮（click()）

browser.close()            #关闭当前窗口
# browser.quit()           #退出并关闭窗口的每一个相关的驱动程序


