#Nathan Gregorian Bailey
#Section 0003
#Program 6
#Created on December 4th 2021 
#Due December 11th 2021



class Store():
    '''Store Class for getting stores location and name'''
    def __init__(self,name='None',location='None'):
        '''constructor of store class'''
        self.name = name
        self.location = location
    def setter(self,storeName,storeLocation):
        '''setter of store class'''
        self.name = storeName
        self.location = storeLocation
    def display(self):
        '''display of store class'''
        return 'User placed order from: {}\nAt address: {}'.format(self.name,self.location)

class Cart(Store):
    '''Cart Class for creating the cart as well as adding/removing items and totaling the receipt'''
    def __init__(self,name,location,productName='',quantity=0,cart= {'Milk':0,'Bread':0,'Egg':0,'Flour':0,'Oil':0,'Cheese':0},receipt=0):
        '''constructor of cart class'''
        super().__init__(name,location)
        self.productName = productName
        self.quantity = quantity
        self.cart = cart
        self.receipt = receipt
    def Add_item(self,product,quantity):
        '''Add items to cart'''
        self.productName = product
        self.quantity = quantity
        if self.quantity < 0:
            print('You cannot enter a negative amount')
        elif self.productName in self.cart and self.quantity >=0:
            self.cart[self.productName] += int(self.quantity)
        elif self.productName not in self.cart:
            print('Sorry we do not have {} at this Store'.format(self.productName))
    def test_cart(self):
        '''testing cart to make sure it works feel free to ignore'''
        return self.cart
    def Remove_item(self,product,quantity):
        '''Remove items from cart'''
        self.productName = product
        self.quantity = quantity
        if self.quantity < 0:
            print('You cannot enter a negative amount')
        elif self.productName in self.cart and self.cart[self.productName] > 0:
            self.cart[self.productName] -= int(self.quantity)
            if self.cart[self.productName] < 0:
                self.cart[self.productName] = 0
        else:
            print('{} is not in your cart'.format(self.productName))
    def receipt_setter(self,receipt=0,prices=[2.50,1.98,.70,1.18,4.00,2.68] ):
        '''compiling total of receipt and setting it'''
        self.prices = prices
        for x,y in enumerate(self.cart):
            receipt += self.cart[y]*prices[x]
        self.receipt = receipt
        return self.receipt
    def display(self):
        '''display of cart to show what is in it'''
        print('Order in Cart is:')
        for x,y, in enumerate(self.cart):
            if self.cart[y] > 0:
                print('{} with quantity: {}'.format(y,self.cart[y]))
        

#product dictionary list
def product_display():
    products = {'Milk':2.50,
    'Bread':1.98,
    'Egg':0.70,
    'Flour':1.18,
    'Oil':4.00,
    'Cheese':2.68}
    print('Products as follow:')
    for x,y in enumerate(products):
        print('{}: ${:.2f}'.format(y,products[y]))


if __name__ == '__main__':
    b = Store()
    store_name = input('Good morning! Which store you want to use today?\n')
    store_location = input('Which location you want to use?\n')
    b.setter(store_name,store_location)
    print()
    print(b.display())
    print()
    product_display()
    print()
    c = Cart(b.name,b.location)
    adder = input('Do you want to add a product? (yes/no)\n')
    while True:
        if adder.upper() == 'YES':
            product_add = input('Enter name of your product to add\n')
            while True:
                try:
                    amount_add = int(input('Enter quantity\n'))
                    break
                except ValueError:
                    print('please enter an integer such as 1,2,3...do not enter the name of the number or decimals')
            c.Add_item(product_add,amount_add)
            c.display()
            print('Total receipt is ${:.2f}'.format(c.receipt_setter()))
            adder = input('Do you want to add another product (yes/no)\n')
        if adder.upper() == 'NO':
            break
        if adder.upper() != 'YES' and adder.upper() != 'NO':
            print('please enter yes or no')
            adder = input('Do you want to add a product? (yes/no)\n')
    remover = input('Do you want to remove an item? (Yes/No)\n')
    while True:
        if remover.upper() == 'YES':
            product_remove = input('Enter name of your product to remove\n')
            while True:
                try:
                    amount_remove = int(input('Enter quantity\n'))
                    break
                except ValueError:
                    print('please enter an integer such as 1,2,3...do not enter the name of the number or decimals')
            c.Remove_item(product_remove,amount_remove)
            c.display()
            print('Total receipt is ${:.2f}'.format(c.receipt_setter()))
            remover = input('Do you want to remove another item? (Yes/No)\n')
        if remover.upper() == 'NO':
            break
        if remover.upper() != 'YES' and remover.upper() != 'NO':
            print('please enter yes or no')
            remover = input('Do you want to remove a product? (yes/no)\n')
    adder = input('Last Chance before you get your total.  Do you want to add a product? (yes/no)\n')
    while True:
        if adder.upper() == 'YES':
            product_add = input('Enter name of your product to add\n')
            while True:
                try:
                    amount_add = int(input('Enter quantity\n'))
                    break
                except ValueError:
                    print('please enter an integer such as 1,2,3...do not enter the name of the number or decimals')
            c.Add_item(product_add,amount_add)
            c.display()
            print('Total receipt is ${:.2f}'.format(c.receipt_setter()))
            adder = input('Do you want to add another product (yes/no)\n')
        if adder.upper() == 'NO':
            break
        if adder.upper() != 'YES' and adder.upper() != 'NO':
            print('please enter yes or no')
            adder = input('Do you want to add a product? (yes/no)\n')
    print()
    print('Thank you for shopping at {}, located at: {}\nHere is what you have ordered:\n'.format(store_name,store_location))
    c.display()
    if int(c.receipt_setter()) <= 0:
        print('Your Cart is Empty')
    print('Your total receipt is ${:.2f}'.format(c.receipt_setter()))











'''testing program a bit with these'''


#class store start
'''b = Store()
store_name = input('Good morning! Which store you want to use today?\n')
store_location = input('Which location you want to use?\n')
b.setter(store_name,store_location)
print(b.display())'''

#cart add item test
'''c = Cart(b.name,b.location)
product_add = input('Enter name of your product to add\n')
amount_add = int(input('Enter quantity\n'))
c.Add_item(product_add,amount_add)
print(c.test_cart())'''
#cart remove item test
'''product_remove = input('Enter name of your product to remove\n')
amount_remove = input('Enter quantity\n')
c.Remove_item(product_remove,amount_remove)
print(c.test_cart())'''
#display test
'''c.display()
print('Total receipt is ${:.2f}'.format(c.receipt_setter()))'''