#couding=utf-8

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_case(self):
        self.a = "hello"
        self.b = "hello world"
        self.assertIn(self.a, self.b, msg="a is not in b")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()