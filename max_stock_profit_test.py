import unittest, csv

import max_stock_profit as msp

class MaxStockProfitTests(unittest.TestCase):

    def testMaxStockProfit1(self):
        test_prices = [4,6,7,10,23,20,60,30,29,11,17,32,35,36,40]
        self.assertEqual(msp.maxStockProfit(test_prices), 56)

    def testMaxStockProfit2(self):
        test_prices = [4,6,7,10,2,5,60,3,7,8,70,2,3]
        self.assertEqual(msp.maxStockProfit(test_prices), 68)

    def testMaxStockProfit3(self):
        test_prices = [2,6,7,10,2,5,60,3,7,8,70,2,80]
        self.assertEqual(msp.maxStockProfit(test_prices), 78)

    def testMaxStockProfit4(self):
        test_prices = [100,6,7,10,70,1,5,80,1,7,8,70,2,60]
        self.assertEqual(msp.maxStockProfit(test_prices), 79)

    def testMaxStockProfit5(self):
        test_prices = [1,2,3,4,5,6]
        self.assertEqual(msp.maxStockProfit(test_prices), 5)

    def testMaxStockProfit6(self):
        test_prices = [7,6,5,4,3,2]
        self.assertEqual(msp.maxStockProfit(test_prices), 0)

    def testMaxStockProfit7(self):
        test_prices = [7,7,7,7,7,7,7]
        self.assertEqual(msp.maxStockProfit(test_prices), 0)

    def testMaxStockProfit8(self):
        test_prices = [1,2,3,4,5,4,3,2,1]
        self.assertEqual(msp.maxStockProfit(test_prices), 4)

    def testMaxStockProfit9(self):
        test_prices = []
        self.assertEqual(msp.maxStockProfit(test_prices), 0)

    def testMaxStockProfit10(self):
        test_prices = [100, 98, 97, 98, 97, 98, 99, 100, 110, 100, 108, 99, 98]
        self.assertEqual(msp.maxStockProfit(test_prices), 13)
