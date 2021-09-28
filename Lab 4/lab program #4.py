#Lab 4
#Nathan Bailey
#Section 0003
#September 28th 2021
import random

def play_again(): #This function allows the User to "play again".
    playAgain = input('Do you want to play again? Y or YES to continue, N or NO to quit\n')
    while True:
        if playAgain.upper() == 'Y':
            return True 
        if playAgain.upper() == 'YES':
            return True
        elif playAgain.upper() == 'N':
            return False
        elif playAgain.upper() == 'NO':
            return False
        else:
            playAgain = input('Please input correct inputs only.  Do you want to play again? Y or YES to continue, N or NO to quit\n')

def get_wager(bank : chips): #function to return an integer
    chips = int(input('How many chips would you like to wager?\n'))
    checkerchips = -1
    while checkerchips == -1:
        if chips <= 0:
            print('Please input a value greater than 0')
            chips = int(input('How many chips would you like to wager?\n'))
        else:
            checkerchips = 200

def get_slot_results():
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    slotresult = (x,y,z)
    return slotresult


def get_mactches(reela, reelb, reelc):
    if reela == reelb == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank():
    bank = int(input('How many chips do you want to start with?\n'))
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
        payout = wager*10 - wager
    if matches == 2:
        payout = wager*3 - wager
    else:
        payout = -1*wager
    return payout

