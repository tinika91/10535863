# -*- coding: utf-8 -*-
"""
Created on Fri April  17 15:25:57 2020

@author: tinal
"""
import csv
from carApplicationFleet_CA2 import *
from carApplicationCar_CA2 import *

class Customer(Car, CarFleet):

    def __init__(self, name = '', address ='', age = 0, licenceNumber=''):
    
        Car.__init__(self)
        CarFleet.__init__(self)
        self.cars = 0
        self.rentalCode = 0

    # Getting an information about customer    
    def inputData(self):
        
        print('====== Customer Information =======')
        self.name = input('\nEnter your name and surname: ')
        self.address = input('\nEnter your address: ')
        self.age = input('\nEnter your age: ')
        self.licenceNumber = input('\nEnter your licence number: ')
        
        customerData = [{'Name and Surname': self.name, 'Address': self.address, 'Age': self.age, 'Licence Number': self.licenceNumber}]
 
        fields = ['Name and Surname', 'Address', 'Age', 'Licence Number']
        
        with open('Car_Rental_Customer_Information.csv', mode='w') as csvfile:  

            writer = csv.DictWriter(csvfile, fieldnames = fields)  
            writer.writeheader()  
            writer.writerows(customerData)  
 
           
    # Customer request for a car
    def requestCar(self):
        rentedCar = None
        result = 0
        
        typ = input('\nWhat car would you like to rent? \nPetrol Car Enter - P \nElectric Car - E \n'
                    'Diesel Car - D \nHybrid Car - H \n\n Enter: ')
        list = ['P', 'E', 'D', 'H']
        if typ.upper() in list:
            rentedCar = (input('How many car/cars would you like to rent?\n\n Enter: '))
            if rentedCar.isalpha():
                exit()
            else:
                rentedCar = int(rentedCar)
        else:
            exit()
        result = self.rent(typ, rentedCar)
        if result:
            print('\nYou have rented {} car.\n\n'.format(typ))
            self.checkCarsInStock()
        else:
            s = ('\nApologize, there is no {} car available, please rent some other car\n'.format(typ))
            print(s)


    # Customer reguest for a return of a rented car 
    def returnCars(self):
        
        typ = input('\nWhat car would you like to return? \n For Petrol Car Enter - P \n For Electric Car - E \n '
                    'For Diesel Car - D \n For Hybrid Car - H \n\n Enter:  ')
        list = ['P', 'E', 'D', 'H']
        typ = typ.upper()
        if typ in list:
            count = (input('How many car/cars would you like to return? \n\n Enter: '))
            if count.isalpha():
                exit()
            else:
                count = int(count)
        else:
            exit()
        result = self.returnCar(typ, count)
        if result:
            print('\nThank you, you have returned your car/cars.\n\n')
            self.checkCarsInStock()



if __name__ == "__main__":
    function = Customer()
    function.inputData()
    function.requestCar()
    function.returnCars()


