#Nathan Gregorian Bailey
#Section 0003
#Program 8
#Created on October 26th 2021 
#Due October 28th 2021
def test_grades():
    test_score = input('\nEnter the new Test score 0-100 ==> ')
    return test_score

def program_grades():
    program_score = input('\nEnter the new Assignment score 0-100 ==> ')
    return program_score

def program_remove():
    remove = input('\nEnter the Assignment score to remove 0-100 ==> ')
    return remove

def test_remove():
    remove = input('\nEnter the Test score to remove 0-100 ==> ')
    return remove

def menu():
    print()
    print('Grade Menu'.center(50))
    prompt = input('1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n==> ')
    return prompt

def checker_output(x):
    if x.upper() == 'Q':
        return 0

def display(tcount, tmin, tmax, tavg, tstd, pcount, pmin, pmax, pavg, pstd):
    print('Type','#'.center(25),'min'.center(8),'max'.center(8),'avg'.center(8),'std'.center(8))
    print('='*65)
    print('Tests',str(tcount).center(23),str((tmin)).center(9),str((tmax)).center(8),str((tavg)).center(8),str(tstd).center(8))
    print('Programs',str(pcount).center(18),str((pmin)).center(13),str((pmax)).center(4),str((pavg)).center(11),str(pstd).center(6))
    try:
        wscore = float(tavg*.60 + pavg*.40)
    except:
        try: 
            wscore = float(tavg)
        except:
            try:
                wscore = float(pavg)
            except:
                wscore = '0.00'
    print()
    print('The weighted score is',str(wscore).center(30))

def std(x):
    top = 0
    m = sum_def(x)/len(x)
    for i in x:
        top += (int(i) - m)**2
    return round(float((top/len(x))**(1/2)),2)
def sum_def(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

test = []
program = []
checker = -1
while checker == -1:
    tcount = int(len(test))
    pcount = int(len(program))
    try:
        tmin = float(min(test))
    except ValueError:
        tmin = 'n/a'
    try:
        pmin = float(min(program))
    except ValueError:
        pmin = 'n/a'
    try:
        tmax = float(max(test))
    except ValueError:
        tmax = 'n/a'
    try:
        pmax = float(max(program))
    except ValueError:
        pmax = 'n/a'
    try:
        tavg = int(sum_def(test))/int(tcount)
    except ZeroDivisionError:
        tavg = 'n/a'
    try:
        pavg = int(sum_def(program))/int(pcount)
    except ZeroDivisionError:
        pavg = 'n/a'
    try:
        tstd = std(test)
    except ZeroDivisionError:
        tstd = 'n/a'
    try:
        pstd = std(program)
    except ZeroDivisionError:
        pstd = 'n/a'
    prompt = menu()
    if prompt.upper() == 'Q':
        checker = 0
    if prompt.upper() == 'D':
        display(tcount, tmin, tmax, tavg, tstd, pcount, pmin, pmax, pavg, pstd)
    if prompt == '1':
        test.append(test_grades())
    if prompt == '2':
        try:
            test.remove(test_remove())
        except:
            print('Could not find that score to remove')
    if prompt == '3':
        test.clear()
    if prompt == '4':
        program.append(program_grades())
    if prompt == '5':
        try:
            program.remove(program_remove())
        except:
            print('Could not find that score to remove')
    if prompt == '6':
        program.clear()