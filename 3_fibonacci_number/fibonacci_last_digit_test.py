import unittest
import random
from .fibonacci_last_digit import get_fibonacci_last_digit_naive, get_fibonacci_last_digit_fast


class MyTestCase(unittest.TestCase):
    def test_fibonacci_fast_result(self):
        n = random.randint(5, 100)
        self.assertEqual(get_fibonacci_last_digit_naive(n), get_fibonacci_last_digit_fast(n))

    def test_stress_fibonacci_fast(self):
        for i in range(1000):
            print('Loop Number:', i)
            n = random.randint(5, 100000)
            print('Random number generated:', n)
            self.assertEqual(get_fibonacci_last_digit_naive(n), get_fibonacci_last_digit_fast(n))

if __name__ == '__main__':
    unittest.main()
