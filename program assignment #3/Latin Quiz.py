#Nathan Gregorian Bailey
#Section 0003
#Program 3
#Created on October 10th 2021 
#Due October 17th 2021
import random
checker = -1
while checker == -1:
    print('Ready for your Quiz')
    engList = ['water', 'good', 'before noon', 'in fact', 'I', 'sea', 'afternoon']
    latList = ['aqua', 'bene', 'ante meridiem', 'de facto', 'ego', 'mare', 'post meridian']
    q1 = random.randint(0,6)
    q2 = random.randint(0,6)
    q3 = random.randint(0,6)
    while q2 == q1:
        q2 = random.randint(0,6)
    while q3 == q2 or q3 == q1:
        q3 = random.randint(0,6)


    question1 = engList[q1]
    question2 = engList[q2]
    question3 = engList[q3]
    counter = 0
    print('what is {} in Latin?'.format(question1))
    answer1 = input()
    if answer1 == latList[q1]:
        print('Correct')
        counter += 1
    else:
        print('Incorrect')
    print('what is {} in Latin?'.format(question2))
    answer2 = input()
    if answer2 == latList[q2]:
        print('Correct')
        counter += 1
    else:
        print('Incorrect')
    print('what is {} in Latin?'.format(question3))
    answer3 = input()
    if answer3 == latList[q3]:
        print('Correct')
        counter += 1
    else:
        print('Incorrect')
    print('You got {} correct answer(s)'.format(counter))
    checker2 = -1
    while checker2 == -1:
        tryAgain = input('Do you want to play again: Y/y or N/n\n')
        if tryAgain == 'Y' or tryAgain == 'y':
            checker2 = 0
            break
        elif tryAgain == 'N' or tryAgain =='n':
            checker2 = 0
            checker = 0
            print('Have a great day')
            break
        else:
            print('Please input Y/y or N/n all other inputs are invalid')
