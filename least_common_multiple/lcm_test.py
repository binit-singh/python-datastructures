import unittest
import random
from .lcm import lcm_fast, lcm_naive


class LCMTestCase(unittest.TestCase):
    def test_lcm_fast_result(self):
        a = random.randint(5, 100)
        b = random.randint(5, 100)
        self.assertEqual(lcm_naive(a, b), lcm_fast(a, b))

    def test_lcm_stress(self):
        for i in range(10000):
            print('Loop number:', i)
            a = random.randint(5, 100)
            b = random.randint(5, 100)
            print('Numbers:{}, {}'.format(a, b))
            self.assertEqual(lcm_naive(a, b), lcm_fast(a, b))


if __name__ == '__main__':
    unittest.main()