# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:25:57 2020

@author: tinal
"""
import csv
from carApplicationCar_CA2 import *

class CarFleet(object):

    def __init__(self):
        self.__petrol_cars = []
        self.__electric_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []
        self.No_of_petrol_cars_rented = []
        self.No_of_electric_cars_rented = []
        self.No_of_diesel_cars_rented = []
        self.No_of_hybrid_cars_rented = []

        for i in range(1, 21):
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, 11):
            self.__electric_cars.append(ElectricCar())
        for i in range(1, 7):
            self.__diesel_cars.append(DieselCar())
        for i in range(1, 5):
            self.__hybrid_cars.append(HybridCar())

    def getPetrolCars(self):
        return self.__petrol_cars

    def getElectricCars(self):
        return self.__electric_cars

    def getDieselCars(self):
        return self.__diesel_cars

    def getHybridCars(self):
        return self.__hybrid_cars

    def checkCarsInStock(self):
        
        p = ('Number of Petrol Cars   : ' + str(len(self.getPetrolCars())))
        e = ('Number of Electric Cars : ' + str(len(self.getElectricCars())))
        d = ('Number of Diesel Cars   : ' + str(len(self.getDieselCars())))
        h = ('Number of Hybrid Cars   : ' + str(len(self.getHybridCars())))
        print(p)
        print(e)
        print(d)
        print(h)

        with open('Car_Rental_Status.csv', mode='w') as write:
            write.write(p + f' Rented :{len(self.No_of_petrol_cars_rented)}' + '\n')
            write.write(e + f' Rented :{len(self.No_of_electric_cars_rented)}' + '\n')
            write.write(d + f' Rented :{len(self.No_of_diesel_cars_rented)}' + '\n')
            write.write(h + f' Rented :{len(self.No_of_hybrid_cars_rented)}' + '\n')
        return [len(self.getPetrolCars()), len(self.getElectricCars()), len(self.getDieselCars()),
                len(self.getHybridCars()), len(self.No_of_petrol_cars_rented),
                len(self.No_of_electric_cars_rented), len(self.No_of_diesel_cars_rented),
                len(self.No_of_hybrid_cars_rented)]


    def rent(self, type, noOfCars):
        # Petrol car
        if type == 'P':
            if len(self.__petrol_cars) == 0:
                return False
            if noOfCars <= len(self.__petrol_cars):
                for s in range(0, noOfCars):
                    self.No_of_petrol_cars_rented.append(self.__petrol_cars.pop())
                return True

            elif noOfCars > len(self.__petrol_cars):
                for s in range(0, len(self.__petrol_cars)):
                    self.No_of_petrol_cars_rented.append(self.__petrol_cars.pop())
                return True

            return False

        # Electric car        
        elif type == 'E':
            if len(self.__electric_cars) == 0:
                return False
            if noOfCars <= len(self.__electric_cars):
                for s in range(0, noOfCars):
                    self.No_of_electric_cars_rented.append(self.__electric_cars.pop())
                return True

            elif noOfCars > len(self.__electric_cars):
                for s in range(0, len(self.__electric_cars)):
                    self.No_of_electric_cars_rented.append(self.__electric_cars.pop())
                return True

            return False
 
        # Diesel car       
        elif type == 'D':
            if len(self.__diesel_cars) == 0:
                return False
            if noOfCars <= len(self.__diesel_cars):
                for s in range(0, noOfCars):
                    self.No_of_diesel_cars_rented.append(self.__diesel_cars.pop())
                return True

            elif noOfCars > len(self.__diesel_cars):
                for s in range(0, len(self.__diesel_cars)):
                    self.No_of_diesel_cars_rented.append(self.__diesel_cars.pop())
                return True

            return False
        
        # Hybrid car        
        else:
            if len(self.__hybrid_cars) == 0:
                return False
            if noOfCars <= len(self.__hybrid_cars):
                for s in range(0, noOfCars):
                    self.No_of_hybrid_cars_rented.append(self.__hybrid_cars.pop())
                return True

            elif noOfCars > len(self.__hybrid_cars):
                for s in range(0, len(self.__hybrid_cars)):
                    self.No_of_hybrid_cars_rented.append(self.__hybrid_cars.pop())
                return True

            return False


    def returnCar(self, type, noOfCars):
        # Petrol car  
        if type == 'P':
            if self.No_of_petrol_cars_rented:
                if noOfCars >= len(self.No_of_petrol_cars_rented):
                    for s in range(0, len(self.No_of_petrol_cars_rented)):
                        self.__petrol_cars.append(self.No_of_petrol_cars_rented.pop())
                    return True
                else:
                    for s in range(0, noOfCars):
                        self.__petrol_cars.append(self.No_of_petrol_cars_rented.pop())
                    return True
            else:
                print('\nNo car rented.\n')
                return False

        # Electric car  
        elif type == 'E':
            if self.No_of_electric_cars_rented:
                if noOfCars >= len(self.No_of_electric_cars_rented):
                    for s in range(0, len(self.No_of_electric_cars_rented)):
                        self.__electric_cars.append(self.No_of_electric_cars_rented.pop())
                    return True
                else:
                    for s in range(0, noOfCars):
                        self.__electric_cars.append(self.No_of_electric_cars_rented.pop())
                    return True
            else:
                print('\nNo car rented.\n')
                return False
 
        # Diesel car             
        elif type == 'D':
            if self.No_of_diesel_cars_rented:
                if noOfCars >= len(self.No_of_diesel_cars_rented):
                    for s in range(0, len(self.No_of_diesel_cars_rented)):
                        self.__diesel_cars.append(self.No_of_diesel_cars_rented.pop())
                    return True
                else:
                    for s in range(0, noOfCars):
                        self.__diesel_cars.append(self.No_of_diesel_cars_rented.pop())
                    return True
            else:
                print('\nNo car rented.\n')
                return False
 
        # Hybrid car             
        elif type == 'H':
            if self.No_of_hybrid_cars_rented:
                if noOfCars >= len(self.No_of_hybrid_cars_rented):
                    for s in range(0, len(self.No_of_hybrid_cars_rented)):
                        self.__hybrid_cars.append(self.No_of_hybrid_cars_rented.pop())
                    return True
                else:
                    for s in range(0, noOfCars):
                        self.__hybrid_cars.append(self.No_of_hybrid_cars_rented.pop())
                    return True
            else:
                print('\nNo car rented.\n')
                return False


if __name__ == "__main__":
    function = CarFleet()
    function.checkCarsInStock()

