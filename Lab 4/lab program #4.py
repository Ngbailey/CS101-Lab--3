#Lab 4
#Nathan Bailey
#Section 0003
#September 28th 2021
import random
checker = -1
def play_again(): #This function allows the User to "play again".
    playAgain = input('Do you want to play again? Y or YES to continue, N or NO to quit\n')
    cheppers = -1
    while cheppers == -1:
        if playAgain == 'Y':
            cheppers = 200
            return True
        if playAgain == 'YES':
            cheppers = 200
            return True
        elif playAgain == 'N':
            cheppers = 200
            return False
        elif playAgain == 'NO':
            cheppers = 200
            return False
        else:
            playAgain = input('Please input correct inputs only.  Do you want to play again? Y or YES to continue, N or NO to quit\n')


chips = 200
bank = 100
def get_wager(bank , chips): #function to return an integer
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


def get_matches(reela, reelb, reelc):
    if reela == reelb == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank():
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

def get_payout(wager, matches):
    if matches == 3:
        wager += wager*10 - wager
    if matches == 2:
        wager += wager*3 - wager
    else:
        wager -= wager
    return wager

get_bank()
while checker == -1:
    get_wager(bank , chips)
    get_slot_results()
    slotresult = get_slot_results
    for i in slotresult:
        slotresult.append(i)
    x = slotresult[0]
    y = slotresult[1]
    z = slotresult[2]
    get_matches(x,y,z)
    get_payout(get_wager,get_matches(x,y,z))
    play_again()
    checkers = -1
    while checkers == -1:
        if play_again() is True:
            break
        else:
            checkers = 200
            checker = 200
            exit

