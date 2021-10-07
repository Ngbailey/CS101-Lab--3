def get_school(string):
    if string[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif string[5] == '2':
        return 'School of Law'
    elif string[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(string):
    if string[6] == '1':
        return 'Freshman'
    elif string[6] == '2':
        return 'Sophomore'
    elif string[6] == '3':
        return 'Junior'
    elif string[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value(string):
    string = int(ord(string) - 65)

def get_check_digit(string):
    total_digits = 0
    n = 1
    for i in string[0:5]:
        if i.isalpha() == True:
            i = ord(i) - 65
            total_digits += i*n
            n += 1
    n = 6
    for i in string[5:10]:
        if i.isnumeric() == True:
            i = int(i)
            total_digits += i*n
            n += 1
    return total_digits%10




def verify_check_digit(string):
    checker = -1
    while checker == -1:
        if len(string) < 10:
            checker = 2
            return False, "The length of the number given must be 10"
        if len(string) > 10:
            checker = 2
            return False, "The length of the number given must be 10"
        for i in string[0:5]:
            n= 0
            if i.isalpha() is False:
                checker = 2
                return False, "The first 5 characters must be A-Z, the invalid character is at {} is {}".format(i,n)
            else:
                n+=1
        for i in string[7:10]:
            n=7
            if i.isnumeric() is False:
                checker = 2
                return False, "The last 3 characters must be 0-9, the invalid character is at {} is {}".format(i,n)
            else:
                n+=1
        for i in string[5]:
            if i == '1' or i == '2' or i == '3':
                continue
            else:
                checker = 2
                return False, "The sixth character must be 1 2 or 3"
        for i in string[6]:
            if i == '1' or i == '2' or i == '3' or i == '4':
                continue
            else:
                checker = 2
                return False, "The seventh character must be 1 2 3 or 4"
        for i in string[9]:
            if int(i) != get_check_digit(string):
                checker = 2
                return False, "Check Digit {} does not match calculated value {}.".format(i,get_check_digit(string))
            else:
                checker = 2
                return True, ''

print('Linda Hall'.center(100))
print('Libary Card Check'.center(100))
print('='*97)
checker = -1
while checker == -1:
    libCard = str(input('\nEnter Libary Card. Hit Enter to Exit ==>'))
    if libCard == '':
        checker = 2
        break
    verify_check_digit(libCard)
    if verify_check_digit(libCard)[0] == True:
        print('Libary Card is valid.')
        print('The card belongs to a student in {}'.format(get_school(libCard)))
        print('The card belongs to a {}'.format(get_grade(libCard)))
    else:
        print('Libary card is invalid.')
        print(verify_check_digit(libCard)[1])
        

