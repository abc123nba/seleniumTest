#coding=utf-8

import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#定义测试用例的目录
test_dir = './test_case'

#定义测试结果的目录
test_result = './report'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_result + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告',description='用例执行情况： ')
    runner.run(discover)
    fp.close()

############################
"""
python runtest.py >> report/log.txt 2>&1
（1）python runtest.py 通过python执行runtest文件
（2）>> report/log.txt 将测试输出写入到report目录下的log.txt文件中
（3）file 2>&1 标准输出被重定向到文件file，然后错误输出也重定向到和标准输出一样，所有错误输出也写入文件file
"""
#############################