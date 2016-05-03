#couding=utf-8

import unittest
from Unit5.count5 import is_prime

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_case(self):
        self.prime = is_prime(2)
        self.assertTrue(self.prime, msg="Is not prime!")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()