#Nathan Gregorian Bailey
#Section 0003
#Program 4
#Created on October 24th 2021 
#Due October 31st 2021
def customer_file():
    '''function to recive file name'''
    file_name = input('\nEnter file name')
    return file_name

def menu():
    '''function to display menu'''
    print('\n1- Print Transaction ID and user name\n\n2- Print user name , total before and total after discount\n\n3- Quit\n')

def file():
    '''function to aquire the file'''
    checker = -1
    while checker == -1:
        try:
            file_name = input('Enter file name ==> ')
            customer_file = open(file_name)
            customer_lines = customer_file.readlines()
            checker = 0
            print()
            print('\nReading data...\n')
        except IOError:
            print('\nEnter correct file name\n')
            checker = -1
    return customer_lines

def choice1_output(x):
    '''function to output ID and Username'''
    print('{:<5} {:<10} {:<10}\n'.format('ID','FirstName','LastName'))
    for i in x:
        y = i.split()
        print('{:<5} {:<10} {:<10}\n'.format(y[0],y[1],y[2]))

def cont():
    '''function to determine if they want to continue or quit'''
    checker = -1
    while checker == -1:
        x = input('Do you want to see more option Y/N: ')
        if x.upper() == 'Y':
            checker = 0
            return -1
        elif x.upper() == 'N':
            print('\nHave a great day')
            checker = 0
            return 0
        else:
            print('\nInvalid input')
    
def choice2_output(x):
    '''function to output ID, Username, before store discount and after store discount'''
    print('{:<5} {:<10} {:<10} {:<10} {:<10}\n'.format('ID','FirstName','LastName','Before','After'))
    for i in x:
        y = i.split()
        listx = []
        for n in y:
            listx.append(n)
        z = float(listx[-1])
        z1 = round(z - z*(40/100),2)
        print('{:<5} {:<10} {:<10} {:<10} {:<10}\n'.format(y[0],y[1],y[2],y[-1], z1))


checker = -1
while checker == -1:
    menu()
    checker2 = -1
    while checker2 == -1:
        choice = input('Enter your choice ==> ')
        if choice == '1':
            choice1_output(file())
            checker2 = 0
            checker = cont()
        elif choice == '2':
            choice2_output(file())
            checker2 = 0
            checker = cont()
        elif choice == '3':
            checker = 0
            checker2 = 0
            print('\nHave a great day')
        else:
            print('\nEnter valid option\n')
