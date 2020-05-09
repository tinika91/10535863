# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:49:51 2020

@author: tinal
"""

class Billing():
    
    def __init__(self, rentalPeriod=0, baseCharge=0, odoStart=0, odoEnd=0, totalMiles=0, budgetCharge='', dailyCharge='', weeklyCharge=''):

        self.rentalPeriod = rentalPeriod

        self.baseCharge = baseCharge

        self.odoStart = odoStart
        
        self.odoEnd = odoEnd
        
        self.totalMiles = totalMiles

    # Base cost for each rental code
        self.budgetCharge = 40.00
        self.dailyCharge = 60.00
        self.weeklyCharge = 190.00



    def totalAmount(self):
        
        print('====== Rental Charge =======')
        
        rentalCode = input('What type of rental would you like? \nBudget - B \nDaily - D \n'
                    'Weekly - W\n\nEnter: ').upper()
        while rentalCode not in ('W', 'D', 'B', 'w', 'd', 'b'):
          print('\nRental code not valid, please re-enter the rental code.\n')

    # Renting period
        if rentalCode == 'W':
          self.rentalPeriod = input('\nNumber of Weeks rented: ');
        elif rentalCode == 'B':
          self.rentalPeriod = input('\nNumber of Days Rented: ');
        elif rentalCode == 'D':
          self.rentalPeriod = input('\nNumber of Days Rented: ');
        
    # Base charge for renting a car 
        if rentalCode == 'B':
          self.baseCharge = int(self.rentalPeriod) * int(self.budgetCharge)
        elif rentalCode == 'D':
          self.baseCharge = int(self.rentalPeriod) * int(self.dailyCharge)
        elif rentalCode == 'W':
          self.baseCharge = int(self.rentalPeriod) * int(self.weeklyCharge)
    
        
    # Distance calculating
        self.odoStart = input('\nStarting odometer reading: ')
        self.odoEnd = input('\nEnding odometer reading: ')
    
        totalMiles = int(self.odoEnd) - int(self.odoStart)
        
    
    # Charges per type of rental    
        if rentalCode == 'B':
          mileCharge = float(totalMiles) * 0.25;  

        elif rentalCode == 'D':
          averageDayMiles = float(totalMiles)/float(self.rentalPeriod);
          if float(averageDayMiles) <= 100:
              extraMiles = 0;
          else:
              extraMiles = float(averageDayMiles) - 100;
          mileCharge = (0.25 * float(extraMiles)) * float(self.rentalPeriod);
    
        elif rentalCode == 'W':
          averageWeekMiles = float(totalMiles)/float(self.rentalPeriod);  
          if averageWeekMiles <= 900:
            mileCharge = 0;
          else:
            mileCharge = 100 * float(self.rentalPeriod);

    # Total amount due
        self.amtDue = float(self.baseCharge) + float(mileCharge)
                   
    
    # Display       
        print('====== Rental Summary Charge =======')
        print('Rental Code:       ' + str(rentalCode))
        print('Rental Period:     ' + str(self.rentalPeriod)) 
        print('Starting Odometer: ' + str(self.odoStart))
        print('Ending Odometer:   ' + str(self.odoEnd))
        print('Miles Driven:      ' + str(totalMiles))
        print('Amount Due:        ' + '€' + str(self.amtDue) + '0')



if __name__ == "__main__":
    function = Billing()
    function.totalAmount()


