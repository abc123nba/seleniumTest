from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep


class Baidu(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        dr = self.dr
        dr.get(self.base_url)
        dr.find_element_by_id("kw").clear()
        dr.find_element_by_id("kw").send_keys("HTMLTestRunner")
        dr.find_element_by_id("su").click()


    def tearDown(self):
        self.dr.close()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    #定义报告存放路径
    fp = open('./result.html', 'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况： ')

    runner.run(testunit) #运行测试用例
    fp.close()


