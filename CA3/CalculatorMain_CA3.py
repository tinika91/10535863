# -*- coding: utf-8 -*-
"""
Created on Fri April  24 19:53:27 2020

@author: tinal
"""

import math
from functools import reduce


class Calculator:
    def __init__(self):
        self.num = 0
        self.values = []
        self.option = 0

    def get_input(self, count):
        for s in range(0, count):
            self.num = int(input('Enter Number: '))
            self.num = int(self.num)
            if int(self.option) == 4:
                if not s == 0:
                    if not self.num == 0:
                        self.values.append(self.num)
                else:
                    self.values.append(self.num)
            else:
                self.values.append(self.num)

    def show_operations(self):
        print("""
        ====== Calculator =======
        
        Please choose from the following:
            
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Modulo
        6. Square
        7. Exponents
        8. Log
        9. Square Root
        0. Factorial
        """)
        
        
    def manage_options(self):
        self.option = int(input('Select operations: '))
        self.select_option()

    def select_option(self):
        if self.option == 1:
            count = int(input('Enter for how many numbers you want to add : '))
            self.get_input(count)
            print('Answer is {}'.format(self.sum()))
            return

        elif self.option == 2:
            count = int(input('Enter for how many numbers you want to subtract : '))
            self.get_input(count)
            print('Answer is {}'.format(self.subtract()))
            return

        elif self.option == 3:
            count = int(input('Enter for how many numbers you want to multiply : '))
            self.get_input(count)
            print('Answer is {}'.format(self.multiplication()))
            return

        elif self.option == 4:
            count = int(input('Enter for how many numbers you want to divide : '))
            self.get_input(count)
            if self.num == 0:
                print('You can not divide with 0\n')
                Calculator()
            else:
                print('Answer is {}'.format(self.div()))
                return 

        elif self.option == 5:
            count = int(input('Enter for how many numbers you want to get mod : '))
            self.get_input(count)
            print('Answer is {}'.format(self.mod()))
            return
        
        elif self.option == 6:
            count = 1
            self.get_input(count)
            print('Answer is {}'.format(self.square()))
            return
        
        elif self.option == 7:
            count = 1
            self.get_input(count)
            exp = int(input('Enter exponent value : '))
            print('Answer is {}'.format(self.exp(exp)))
            return
        
        elif self.option == 8:
            count = 1
            self.get_input(count)
            print('Answer is {}'.format(self.log()))
            return
        
        elif self.option == 9:
            count = 1
            self.get_input(count)
            print('Answer is {}'.format(self.sqrRoot()))
            return
        
        elif self.option == 0:
            count = 1
            self.get_input(count)
            print('Answer is {}'.format(self.fac()))
            return
        

    def sum(self):
        return reduce(lambda x, y: x + y, self.values)

    def subtract(self):
        return reduce(lambda x, y: x - y, self.values)

    def multiplication(self):
        return reduce(lambda x, y: x * y, self.values)

    def div(self):
        if self.values == 0:
            raise ValueError(eval('You can not divide with 0!'))
        else:
            return reduce(lambda x, y: x / y, self.values)

    def mod(self):
        return reduce(lambda x, y: x % y, self.values)

    def square(self):
        sq = map(lambda x: x * x, self.values)
        return next(sq)

    def exp(self, y):
        sq = map(lambda x: x ** y, self.values)
        return next(sq)

    def log(self):
        sq = map(lambda x: math.log10(x), self.values)
        return next(sq)

    def sqrRoot(self):
        sq = map(lambda x: math.sqrt(x), self.values)
        return next(sq)

    def fac(self):
        sq = map(lambda x: math.factorial(x), self.values)
        return next(sq)



if __name__ == "__main__":
    obj = Calculator()
    obj.show_operations()
    obj.manage_options()


