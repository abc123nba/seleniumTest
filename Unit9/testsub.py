#coding=utf-8

import unittest
from Unit9.count9 import Count

class TestSub(unittest.TestCase):
    def setUp(self):
        pass

    #测试整数相减
    def test_sub(self):
        self.j = Count(2, 3)
        self.sub = self.j.sub()
        self.assertEqual(self.sub, -1)

    #测试小数相减
    def test_sub2(self):
        self.j = Count(4.2, 2.2)
        self.sub = self.j.sub()
        self.assertEqual(self.sub, 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)