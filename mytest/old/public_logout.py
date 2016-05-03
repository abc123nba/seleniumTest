#coding=utf-8
from selenium import webdriver
from time import sleep

def logout(dr):
    url = 'http://116.211.105.54:8080/jira/secure/Dashboard.jspa'
    dr.get(url)
    dr.find_element_by_xpath('html/body/div[1]/header/nav/div/div[2]/ul/li[3]/a/span/span/img').click()
    dr.find_element_by_id('log_out').click()
    sleep(3)
    dr.find_element_by_partial_link_text('重新登录').click()
    sleep(5)