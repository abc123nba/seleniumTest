#coding=utf-8

# from selenium import webdriver
# from selenium.webdriver.common.by import By
from PageObject.LoginPage import LoginPage

def test_user_login(driver, username, password):
    """
    测试获取的用户名/密码是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()