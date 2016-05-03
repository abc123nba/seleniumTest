from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


class Baidu(unittest.TestCase):
    '''百度搜索测试'''

    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        '''搜索关键字：HTMLTestRunner'''
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

    #按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    #定义报告存放路径
    filename = './' + now + 'result.html'
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况： ')

    runner.run(testunit) #运行测试用例
    fp.close()


# 执行方式：alt+shfit+F10
"""
发现了问题所在，是软件使用问题运行脚本，楼主一定是用了快捷键CTRL+SHIFT+F10
切记，要用ALT+SHIFT+F10，然后去选择你的脚本的文件名字，去执行。就一切正常了！
在遇到单元测试框架的时候，测试用例本身和下面的执行过程，是分开执行的。
就是说if __name__=="__main__"下面的执行过程是不被执行的。
只是执行了面用例的脚本部分。
"""

