#Nathan Gregorian Bailey
#Section 0003
#Lab 7
#Created on October 19th 2021 
#Due October 21st 2021
checker = -1
while checker == -1:
    try:
        minMPG = float(input('Enter the minimum mpg ==>'))
        if minMPG >= 100:
            print('Fuel economy must be less than 100')
        if minMPG <= 0:
            print('Fuel economy given must be greater than 0')
        if minMPG < 100 and minMPG > 0:
            checker = 0
    except ValueError:
        print('You must enter a number for the fuel economy')


checker2 = -1
while checker2 == -1:
    try:
        inputFile = input('Enter the name of the input vehicle file ==>')
        carFile = open(inputFile)
        checker2 = 0
    except IOError:
        print('Could not open file {}'.format(inputFile))
        checker2 = -1
    if checker2 == 0:
        try:
            lines = carFile.readlines()
            checker2 = 0
        except:
            print('File Not Found')
            checker2 = -1


checker3 = -1
while checker3 == -1:
    try:
        outFile = input('Enter the name of the file to output to ==>')
        wFile = open(outFile, 'w')
        checker3 = 0
    except IOError:
        print('There is an IO Error {}'.format(outFile))
        checker3 = -1
for i in lines:
    blah = i.split()
    bleh = blah[:]
    if bleh[-3].isnumeric():
        bleh = int(bleh[-3])
        if bleh >= minMPG:
            bonk = str('{} {} {:<10} {:>40}\n'.format(blah[0], blah[1], blah[2], blah[-3]))
            wFile.write(bonk)
    elif bleh[-3].isalpha():
        if bleh[-3] == 'combinedmpg':
            continue
        else:
            print('Could not convert value {} for vehicle {} {} {}'.format(blah[-3], blah[0], blah[1], blah[2]))
carFile.close()
wFile.close()
