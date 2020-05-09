# -*- coding: utf-8 -*-
"""
Created on Fri April  17 15:25:57 2020

@author: tinal
"""

class Car(object):

    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def getMileage(self):
        return self.__mileage

    def move(self, distance):
        print('Moved ' + str(distance) + 'kms')
        self.__mileage = self.__mileage + distance

    def paint(self, colour):
        print('Getting a paint job - new colour is: ' + colour)
        self.__colour = colour


class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells


class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''

    def getEngineSize(self):
        return self.__engineSize

    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize


class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''

    def getEngineSize(self):
        return self.__engineSize

    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize


class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        self.__setMoter = ''

    def getEngineSize(self):
        return self.__engineSize

    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize

    def getMoter(self):
        return self.__setMoter

    def setMoter(self, setmoter):
        self.__setMoter = setmoter



if __name__ == "__main__":
    function = Car()

