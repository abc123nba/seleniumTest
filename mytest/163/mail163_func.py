#coding=utf-8

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.implicitly_wait(10)
url = 'http://mail.163.com'
dr.get(url)

#创建表Account类，对用户名和密码进行初始化设置
class Account(object):
    """docstring for Account"""
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

# 创建do_login_as()函数，用于实现用户的登录操作，需要一个user_info参数用于接收用户的登录信息
#取user_info中的username输入到用户名输入框，取user_info中的password输入密码输入框
def do_login_as(user_info):
    dr.find_element_by_id('idInput').clear()
    dr.find_element_by_id('idInput').send_keys(user_info.username)
    dr.find_element_by_id('pwdInput').clear()
    dr.find_element_by_id('pwdInput').send_keys(user_info.password)
    dr.find_element_by_id('loginBtn').click()

#退出函数
def do_logout_as(user_info):
    dr.find_element_by_link_text(u'退出').click()

#实例化登录信息
hcr = Account(username='hcr258', password='hcr20160422')

#调用登录函数
do_login_as(hcr)

sleep(10)

do_logout_as(hcr)

sleep(10)

dr.close()

