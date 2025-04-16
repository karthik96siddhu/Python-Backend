"""
    Encapsulation refers to bundling of attributes and method inside single class.
    It prevents outer classes from accessing and changing attributes and methods of a class. This also helps to achieve data hiding.
    In python private attibutes are denoted using underscore (_ or __)
"""

class Computer:

    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print(f'Selling price : {self.__maxprice}')
    
    def set_max_price(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

# using setter function()
c.set_max_price(1000)
c.sell()

