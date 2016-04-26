#coding=utf-8

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
url = 'https://www.v2ex.com/'
dr.get(url)
dr.implicitly_wait(10)

dr.find_element_by_link_text('登录').click()
sleep(3)

dr.find_element_by_xpath('html/body/div[2]/div[1]/div[3]/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input').send_keys('abc123it')
dr.find_element_by_xpath('html/body/div[2]/div[1]/div[3]/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys('abc12345678')
sleep(3)
dr.find_element_by_xpath('html/body/div[2]/div[1]/div[3]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input[2]').click()
dr.implicitly_wait(10)

dr.find_element_by_link_text('领取今日的登录奖励').click()
dr.find_element_by_xpath('html/body/div[2]/div[1]/div[3]/div[2]/div[2]/input').click()
sleep(3)
dr.find_element_by_xpath('html/body/div[2]/div[1]/div[3]/div[2]/div[3]/input').click()
sleep(10)

dr.close()
