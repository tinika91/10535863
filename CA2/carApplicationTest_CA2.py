# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:16:50 2020

@author: tinal
"""

import unittest
from carApplicationFleet_CA2 import *
from carApplicationCustomer_CA2 import *
from carApplicationBilling_CA2 import *

class TestCar(unittest.TestCase):
    def test_move(self):
        car = Car()
        car.move(5)
        result = car.getMileage()
        self.assertEqual(result, 5)

    def test_paint(self):
        car = Car()
        car.paint('red')
        result = car.getColour()
        self.assertEqual(result, 'red')


class TestFleetCar(unittest.TestCase):
    def test_checkCarsInStock(self):
        carFleet = CarFleet()
        result = carFleet.checkCarsInStock()
        self.assertEqual(result, [20, 10, 6, 4, 0, 0, 0, 0])

    def test_rent(self):
        carFleet = CarFleet()
        carFleet.rent('P', 3)
        result = carFleet.checkCarsInStock()
        self.assertEqual(result, [17, 10, 6, 4, 3, 0, 0, 0])

    def test_returnCar(self):
        carFleet = CarFleet()
        result = carFleet.returnCar('P', 3)
        self.assertEqual(result, False)



if __name__ == "__main__":
    unittest.main()
