#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.page_model import Page

class LoginPage(Page):
    """
    163邮箱登录页面模型
    """
    url = '/'

    #定位器
    username_loc = (By.ID, "idInput")
    password_loc = (By.ID, "pwdInput")
    submit_loc = (By.ID, "loginBtn")

    #Action
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()