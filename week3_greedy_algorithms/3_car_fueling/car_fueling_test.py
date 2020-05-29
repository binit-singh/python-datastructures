import unittest
from .car_fueling import compute_min_refills


class CarFuelingTestCase(unittest.TestCase):
    def test1(self):
        d = 500
        t = 200
        n = 4
        stops = [100, 200, 300, 400]
        refill = compute_min_refills(d, t, stops)
        self.assertEqual(refill, 2)

    def test2(self):
        d = 200
        t = 250
        n = 2
        stops = [100, 150]
        refill = compute_min_refills(d, t, stops)
        self.assertEqual(refill, 0)

    def test3(self):
        d = 950
        t = 400
        n = 4
        stops = [200, 375, 550, 750]
        refill = compute_min_refills(d, t, stops)
        self.assertEqual(refill, 2)

    def test4(self):
        d = 700
        t = 200
        n = 4
        stops = [100, 200, 300, 400]
        refill = compute_min_refills(d, t, stops)
        self.assertEqual(refill, -1)


if __name__ == '__main__':
    unittest.main()
