import unittest
from client3 import getDataPoint, getRatio
from test_data import price, quote


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        assert getDataPoint(quote['normal'])[3] == 120.84

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        assert getDataPoint(quote['bid_greater_than_ask'])[3] == 119.84

    def test_getRatio_calculateRatio(self):
        assert getRatio(price['a'], price['b']) == 0.5

    def test_getRatio_divideByZero(self):
        with self.assertRaises(ValueError):
            getRatio(price['a'], 0)

    def test_getRatio_invalidPrice(self):
        with self.assertRaises(ValueError):
            getRatio(price['a'], '0')


if __name__ == '__main__':
    unittest.main()
