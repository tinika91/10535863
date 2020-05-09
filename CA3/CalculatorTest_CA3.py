# -*- coding: utf-8 -*-
"""
Created on Fri April  24 19:54:43 2020

@author: tinal
"""
import unittest

from CalculatorMain_CA3 import Calculator

c = Calculator()
c.values = [1, 2, 3, 4]


class calculatorTest(unittest.TestCase):
    def test_sum(self):
        res = c.sum()
        self.assertEqual(res, 10)

    def test_sub(self):
        res = c.subtract()
        self.assertEqual(res, -8)

    def test_mul(self):
        res = c.multiplication()
        self.assertEqual(res, 24)

    def test_div(self):
        res = c.div()
        self.assertEqual(res, 0.041666666666666664)

    def test_mod(self):
        res = c.mod()
        self.assertEqual(res, 1)

    def test_sqr(self):
        res = c.square()
        self.assertEqual(res, 1)

    def test_sqRoot(self):
        res = c.square()
        self.assertEqual(res, 1)

    def test_fac(self):
        res = c.fac()
        self.assertEqual(res, 1)

    def test_log(self):
        res = c.log()
        self.assertEqual(res, 0)

    def test_exp(self):
        res = c.exp(1)
        self.assertEqual(res, 1)


if __name__ == "__main__":
    unittest.main()
