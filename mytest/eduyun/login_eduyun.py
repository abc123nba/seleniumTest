# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from time import sleep
import re

class LoginEduyun(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://m.eduyun.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_eduyun(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php?r=portal/site/index")
        driver.find_element_by_id("info_username").click()
        driver.find_element_by_id("info_username").clear()
        driver.find_element_by_id("info_username").send_keys("wangxiaoming")
        driver.find_element_by_id("info_password").clear()
        driver.find_element_by_id("info_password").send_keys("12345678")
        driver.find_element_by_xpath(u"//input[@value='登录']").click()
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector(".optA").click()
        sleep(3)
        driver.find_element_by_css_selector(".dropOpt>dt>a").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
