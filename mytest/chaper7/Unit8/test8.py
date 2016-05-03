#coding=utf-8

import unittest
from Unit8.count8 import Count

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass

    #测试整数相加
    def test_add(self):
        self.j = Count(2, 3)
        self.add = self.j.add()
        self.assertEqual(self.add, 5)

    #测试小数相加
    def test_add2(self):
        self.j = Count(2.3, 4.2)
        self.add = self.j.add()
        self.assertEqual(self.add, 6.5)

    #测试字符串相加
    def test_add3(self):
        self.j = Count("hello"," world")
        self.add = self.j.add()
        self.assertEqual(self.add, "hello world")

    def tearDown(self):
        pass


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
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestAdd("test_add3"))

    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)