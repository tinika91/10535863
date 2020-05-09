# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:16:50 2020

@author: tinal
"""
import sys

from carApplicationCar_CA2 import *
from carApplicationFleet_CA2 import *
from carApplicationCustomer_CA2 import *
from carApplicationBilling_CA2 import *


def mainMenu():
    rental = CarFleet()
    customer = Customer()
    billing = Billing()
    
    while True: 
        print("""
        ====== Dublin Bussiness Car Rental =======
        
        Please choose from the following:
            
        1. Enter Customer Data
        2. Display available cars
        3. Rent a car
        4. Show total cost
        5. Return a car
        6. Exit
        """)

        choice = input('Enter choice: ')
        try:
            choice = int(choice)
        except ValueError:
            print('That is not an integer!')
            continue    
    
        if choice == 1:
            customer.inputData()

        elif choice == 2:
            rental.checkCarsInStock()

        elif choice == 3:
            customer.requestCar()

        elif choice == 4:
            billing.totalAmount() 
            
        elif choice == 5:
            customer.returnCars()
            
        elif choice == 6:
            sys.exit('Thank you for using our car rental system.')
        else:
            print('Invalid input. Please enter number between 1-6 ')
 

if __name__=="__main__":
    mainMenu()
