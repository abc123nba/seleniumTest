#coding=utf-8

from selenium import webdriver
from time import sleep

file_info = open('info.txt', 'r')
values = file_info.readlines()
file_info.close()

for search in values:
    dr = webdriver.Firefox()
    dr.implicitly_wait(10)
    url = 'http://www.baidu.com'
    dr.get(url)
    dr.find_element_by_id('kw').clear()
    dr.find_element_by_id('kw').send_keys(search)
    dr.find_element_by_id('su').click()
    dr.close()


