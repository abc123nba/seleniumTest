#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)

data = driver.find_element_by_id("cp").text
print(data)
time.sleep(3)

driver.close()