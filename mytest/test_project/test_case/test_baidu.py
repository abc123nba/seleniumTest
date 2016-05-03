#coding=utf-8

from selenium import webdriver
import unittest
from time import sleep

class MyTest(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu(self):
        dr = self.dr
        dr.get(self.base_url + "/")
        dr.find_element_by_id("kw").clear()
        dr.find_element_by_id("kw").send_keys("unittest")
        dr.find_element_by_id("su").click()
        sleep(5)
        title = dr.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.dr.close()

if __name__ == '__main__':
    unittest.main()
