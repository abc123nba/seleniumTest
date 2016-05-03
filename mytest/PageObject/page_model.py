#coding=utf-8

# from selenium import webdriver
# from selenium.webdriver.common.by import By

class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'http://mail.163.com'

    def __init__(self, driver, base_url=login_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' %url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)