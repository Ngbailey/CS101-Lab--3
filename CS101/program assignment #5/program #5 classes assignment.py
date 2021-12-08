#Nathan Gregorian Bailey
#Section 0003
#Program 5
#Created on November 15th 2021 
#Due November 21st 2021
from datetime import datetime

class House():
    '''Class for the House information'''
    def __init__(self,year=0,purchase_price=0,currentYear=2021,location='none'):
        self.year = year
        self.purchase_price = purchase_price
        self.location = location
        self.currentYear = currentYear
        self.currentValue = 0
    def current_value(self):
        self.currentValue = int(self.purchase_price * (1 +.08)**(self.currentYear - self.year))
        return self.currentValue
    def __str__(self):
        return 'House Information:\n Year Built: {}\n Purchase Price: {}\n Current Value of House: {}\n Location: {}'.format(self.year, self.purchase_price,self.current_value(),self.location)
    def money_earned(self):
        profit = self.current_value() - self.purchase_price
        return 'Total value you will earn:\n {}'.format(profit)

def info_input():
    '''gather the users information on house'''
    yearcheck = datetime.now().year
    print('Welcome to our house calculation app')
    while True:
        try:
            house_year = int(input('Enter House model year: '))
            if house_year <= 0 or house_year > yearcheck:
                print('Enter a valid year')
            else:
                break
        except ValueError:
            print('Please enter an integer only i.e. "1996"')
    while True:
        try:
            house_price = int(input('Price of the house: '))
            if house_price <= 0:
                print('Enter a valid price')
            else:
                break
        except ValueError:
            print('Please only enter an integer with no other symbols')
    while True:
        try:
            currentYear = int(input('Current Year: '))
            if currentYear < house_year or currentYear != yearcheck:
                print('Enter the correct current year')
            else:
                break
        except ValueError:
            print(' please enter a number for the year i.e. "2021"')
    house_loc = input('Enter your house Location: ')
    return house_year,house_price,currentYear,house_loc







if __name__ == "__main__":
    while True:
        a,b,c,d = info_input()
        print('-'*(17))
        house_information = House(a,b,c,d)
        print(house_information)
        print('-'*(17))
        print()
        print('-'*(34))
        house_profits = house_information.money_earned()
        print(house_profits)
        print('-'*(34))
        while True:
            cont = str(input('Do you want to check price of another house? Y/N: '))
            if cont.upper() == 'Y' or cont.upper() == 'N':
                break
            else:
                print('please enter "Y" or "N".')
        if cont.upper() == 'N':
            break

