#coding=utf-8

from selenium import webdriver
# from selenium.webdriver.common.by import By
from PageObject.test_user_login import test_user_login

def main():
    try:
        driver = webdriver.Firefox()
        username = 'hcr258'
        password = 'qmd20160502'
        test_user_login(driver, username, password)
        driver.implicitly_wait(15)
        text = driver.find_element_by_css_selector("#spnUid").text
        # assert(text == 'hcr258@163.com'), "用户名称不匹配，登录失败！"
        assert (text == (username + '@163.com')), "用户名称不匹配，登录失败！"
    finally:
        #关闭浏览器窗口
        driver.close()


if __name__ == '__main__':
    main()