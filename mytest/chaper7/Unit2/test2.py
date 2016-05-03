#coding=utf-8

from Unit2.count2 import Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        self.j = Count(2, 3)

    def test_add(self):
        self.add = self.j.add()
        self.assertEqual(self.add , 5)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()