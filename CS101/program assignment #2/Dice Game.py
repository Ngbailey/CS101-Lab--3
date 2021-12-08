#Nathan Gregorian Bailey
#Section 0003
#Program 2
#Created on September 17th 2021 (Last Editted September 25th 2021)
#Due September 26th 2021




import random
checker = -1
while checker == -1:
    compRandom = random.randint(1,6)
    userRandom = random.randint(1,6)
    round = 1
    total = userRandom + compRandom
    print('Round 1:')
    print('First dice: {}'.format(compRandom))
    print('Second dice: {}'.format(userRandom))
    if compRandom == userRandom:
        print('**COMPUTER WON!!**')
        print('First dice == Second dice after 1 round')
        print('Total is {}'.format(total))
    else:
        while compRandom != userRandom:
            userRandom = random.randint(1,6)
            round += 1
            total = compRandom + userRandom
            print('Round {}:'.format(round))
            print('First dice: {}'.format(compRandom))
            print('Second dice: {}'.format(userRandom))
        if compRandom == userRandom and round < 3:
            print('**COMPUTER WON!!**')
            print('First dice == Second dice after {} rounds'.format(round))
            print('Total is {}'.format(total))
        if compRandom == userRandom and round >= 3:
            print('**COMPUTER LOST!!**')
            print('First dice == Second dice after {} rounds'.format(round))
    playAgain = input('Do you want to play again? Y to continue, N to quit\n')
    while checker == -1:
        if playAgain == 'Y': 
            break
        elif playAgain == 'N':
            print('Have a great day')
            checker = 200
            exit
            break
        else:
            print('please input "Y" or "N" any other input will not be accepted')
            playAgain = input('Do you want to play again? Y to continue, N to quit\n')
        