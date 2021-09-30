#Lab 4
#Nathan Bailey
#Section 0003
#September 28th 2021
import random
checker = -1
#Play again function#
def play_again():
    cheppers = -1
    while cheppers == -1:
        playAgain = input('Do you want to play again? Y or YES to continue, N or NO to quit==>')
        if playAgain == 'Y' or playAgain == 'YES':
            cheppers = 200
            return True
        elif playAgain == 'N' or playAgain == 'NO':
            cheppers = 0
            return False
        else:
            print('Please input Y/YES or N/NO only.')
    
#get wager function#
def get_wager(bank:int)->int:
    chips = int(input('How many chips would you like to wager?==>'))
    checkerchips = -1
    while checkerchips == -1:
        if chips <= 0:
            print('Please input a value greater than 0')
            chips = int(input('How many chips would you like to wager?==>'))
        if chips > bank:
            print('you cannot wager more than you have.')
            chips = int(input('How many chips would you like to wager?==>'))
        else:
            chips = 1*chips
            checkerchips = 200
            return chips
#Slot result function#
def get_slot_results():
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    slotresult = (x,y,z)
    print('Your spin ',end='')
    for i in slotresult:
        print(i,end=' ')
    print()
    return slotresult
#matching function#
def get_matches(x,y,z):
        if x == y == z:
            matches = 3
        elif x == y or x == z or y == z:
            matches = 2
        else:
            matches = 0
        return matches
#Starting chips function#
def get_bank():
    checkers =-1
    bank = int(input('How many chips do you want to start with?==>'))
    while checkers == -1:
        if bank <= 0:
            print('Too low a value, you can only choose 1 -100 chips')
            bank = int(input('How many chips do you want to start with?==>'))
        if bank >= 101:
            print('Too high a value, you can only choose 1 -100 chips')
            bank = int(input('How many chips do you want to start with?==>'))
        else:
            bank = 1*bank
            checkers = 200
            return bank
#payout function#
def get_payout(chips,matches):
    if matches == 3:
        print('JACKPOT you won {} chips\n'.format(chips*10-chips))
        chips += chips*9 - chips
        return chips
    if matches == 2:
        print('you won {} chips\n'.format(chips*3-chips))
        chips += chips*2 - chips
        return chips
    else:
        print('Sorry you lost {} chips\n'.format(chips))
        chips -= 2*chips
        return chips
    


bank = get_bank()
while checker ==-1:
    chips = get_wager(bank)
    x,y,z = get_slot_results()
    matches = get_matches(x,y,z)
    if matches >= 2:
        bank += get_payout(chips,matches)
    else:
        bank += get_payout(chips,matches)
    print('You have {} chips left\n'.format(bank))
    if play_again() == True:
        checker = -1
    else:
        checker = 200
        exit
        
