print('Welcome to the Flarsheim Guesser!')
playAgain = Y
while playAgain == Y:
    print('Please think of a number between and including 1 and 100.\n')
    computerNumber = list(range(1,101)) #Creating a list from 1 to 100
        ### setting remainder 3 to be within parameters ###
    remainder3 = int(input('What is the remainder when your number is divided by 3 ?\n'))
    while remainder3 < 0:
        print('The value entered must be 0 or greater')
        remainder3 = int(input('What is the remainder when your number is divided by 3 ?\n'))
        while remainder3 >= 3:
            print('The value entered must be less than 3')
            remainder3 = int(input('What is the remainder when your number is divided by 3 ?\n'))
    while remainder3 >= 3:
        print('The value entered must be less than 3')
        remainder3 = int(input('What is the remainder when your number is divided by 3 ?\n'))
        while remainder3 < 0:
            print('The value entered must be 0 or greater')
            remainder3 = int(input('What is the remainder when your number is divided by 3 ?\n'))




    ### Remainder 5
    remainder5 = int(input('What is the remainder when your number is divided by 5 ?\n'))
    while remainder5 < 0:
        print('The value entered must be 0 or greater')
        remainder5 = int(input('What is the remainder when your number is divided by 5 ?\n'))
        while remainder5 >= 5:
            print('The value entered must be less than 5')
            remainder5 = int(input('What is the remainder when your number is divided by 5 ?\n'))
    while remainder5 >= 5:
        print('The value entered must be less than 5')
        remainder5 = int(input('What is the remainder when your number is divided by 5 ?\n'))
        while remainder5 < 0:
            print('The value entered must be 0 or greater')
            remainder5 = int(input('What is the remainder when your number is divided by 5 ?\n'))


    ### Remainder 7
    remainder7 = int(input('What is the remainder when your number is divided by 7 ?\n'))
    while remainder7 < 0:
        print('The value entered must be 0 or greater')
        remainder7 = int(input('What is the remainder when your number is divided by 7 ?\n'))
        while remainder7 >= 7:
            print('The value entered must be less than 7')
            remainder7 = int(input('What is the remainder when your number is divided by 7 ?\n'))
    while remainder7 >= 7:
        print('The value entered must be less than 7')
        remainder7 = int(input('What is the remainder when your number is divided by 7 ?\n'))
        while remainder7 < 0:
            print('The value entered must be 0 or greater')
            remainder7 = int(input('What is the remainder when your number is divided by 7 ?\n'))
    for i in computerNumber:
        if i % 3 != remainder3:
            computerNumber.remove(i)
            for i in computerNumber:
                if i % 5 != remainder5:
                    computerNumber.remove(i)
                    for i in computerNumber:
                        if i % 7 != remainder7:
                            computerNumber.remove(i)
                            for i in computerNumber:
                                if i % 3 != remainder3:
                                    computerNumber.remove(i)
                                    for i in computerNumber:
                                        if i % 5 != remainder5:
                                            computerNumber.remove(i)
                                            for i in computerNumber:
                                                if i % 7 != remainder7:
                                                    computerNumber.remove(i)
    print('Your number was', computerNumber)
    print('How amazing is that?\n')
    playAgain = input('Do you want to play again? Y to continue, N to quit\n')

