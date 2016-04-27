#coding=utf-8

import unittest

def creatsuite():
    testunit = unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir = 'D:\\work\\seleniumTest'
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)

    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

if __name__ == '__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run()