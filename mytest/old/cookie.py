#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os
if 'HTTP_PROXY' in os.environ:
    del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()

url = 'http://www.baidu.com'
dr.get(url)

# dr.find_element_by_link_text('登录').click()
# sleep(3)
# dr.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('839623781@qq.com')
# dr.find_element_by_id('TANGRAM__PSP_8__password').send_keys('abc1234567890')
# dr.find_element_by_id('TANGRAM__PSP_8__submit').click()
# sleep(3)
# dr.find_element_by_xpath('html/body/div[9]/div[2]/div[1]/div/a').click()

cookie = dr.get_cookies()
print(cookie)
dr.delete_all_cookies()

dr.add_cookie({'name':'BAIDUID','value':'AC38766B6B20453F37EF6744798C3DD8:FG=1'})
dr.add_cookie({'name':'BDUSS','value':'1RPOEpTak5LSEhFbEllc01pWlhXeWN0cFJMaWxJTVhPYmVtclExamVzNDZ6anRYQVFBQUFBJCQAAAAAAAAAAAEAAADqPjEnwejP9sfgzOwxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADpBFFc6QRRXd'})

dr.get(url)
sleep(5)

dr.close()