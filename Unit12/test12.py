#coding=utf-8

from Unit12.count12 import Count
import unittest

class TestBdd(unittest.TestCase):
    def setUp(self):
        pass

    #测试整数相加
    def test_ccc(self):
        self.j = Count(2, 3)
        self.add = self.j.add()
        self.assertEqual(self.add, 5)
        print('test1')

    #测试字符串相加
    def test_aaa(self):
        self.j = Count("hello"," world")
        self.add = self.j.add()
        self.assertEqual(self.add, "hello world")
        print('test3')

    def tearDown(self):
        pass


class TestAdd(unittest.TestCase):
    def setUp(self):
        pass

    #测试小数相加
    def test_bbb(self):
        self.j = Count(2.3, 4.2)
        self.add = self.j.add()
        self.assertEqual(self.add, 6.5)
        print('test2')

    def tearDown(self):
        pass

if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestBdd("test_ccc"))    #test1
    suite.addTest(TestAdd("test_bbb"))    #test2
    suite.addTest(TestBdd("test_aaa"))    #test3

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)