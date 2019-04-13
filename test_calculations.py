import unittest
import calculations


class Tests(unittest.TestCase):
    # unit tests for calculation functions
    def test_start_amt_for_good_portfolio(self):
        result = calculations.recommend_start_amt(40000, 20, 0.08)
        expected = 1551034.07
        self.assertEqual(result, expected)

    def test_start_amt_for_bad_portfolio(self):
        result = calculations.recommend_start_amt(100000, 40, 0.01)
        expected = 2410728.87
        self.assertEqual(result, expected)

    def test_withdrawal_for_large_portfolio(self):
        result = calculations.recommend_withdrawal(10000000)
        expected = (350000.0, 450000.0)
        self.assertEqual(result, expected)

    def test_withdrawal_for_small_portfolio(self):
        result = calculations.recommend_withdrawal(50000)
        expected = (1750.0, 2250.0)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
