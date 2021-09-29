import random
checker = -1
bank = int(input('How many chips do you want to start with?'))
while bank <=0 or bank >= 101:
    if bank <= 0:
        print('Too low a value, you can only choose 1 -100 chips')
        bank = int(input('How many chips do you want to start with?\n'))
    if bank >= 101:
        print('Too high a value, you can only choose 1 -100 chips')
        bank = int(input('How many chips do you want to start with?\n'))
    else:
        break
while checker == -1:
    chips = int(input('How many chips would you like to wager?'))
    checkerchips = -1
    while checkerchips == -1:
        if chips <= 0:
            print('Please input a value greater than 0')
            chips = int(input('How many chips would you like to wager?\n'))
        if chips > bank:
            print('you cannot wager more than you have.')
            chips = int(input('How many chips would you like to wager?\n'))
        else:
            checkerchips = 200
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    slotresult = (x,y,z)
    print('Your spin ',end='')
    for i in slotresult:
        print(i,end=' ')
    print()
    if x == y == z:
        matches = 3
    elif x == y or x == z or y == z:
        matches = 2
    else:
        matches = 0
    if matches == 3:
        print('JACKPOT you won {} chips\n'.format(chips*10-chips))
        bank += chips*10 - chips
    if matches == 2:
        print('you won {} chips\n'.format(chips*3-chips))
        bank += chips*3 - chips
    else:
        print('Sorry you lost {} chips\n'.format(chips))
        bank -= chips
    print('You have {} chips left\n'.format(bank))
    playAgain = input('Do you want to play again? Y or YES to continue, N or NO to quit\n')
    cheppers = -1
    while cheppers == -1:
        if playAgain == 'Y':
            cheppers = 200
            break
        if playAgain == 'YES':
            cheppers = 200
            break
        elif playAgain == 'N':
            cheppers = 200
            checker = 200
            exit
        elif playAgain == 'NO':
            cheppers = 200
            checker = 200
            exit
        else:
            playAgain = input('Please input correct inputs only.  Do you want to play again? Y or YES to continue, N or NO to quit\n')