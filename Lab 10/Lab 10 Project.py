#Nathan Gregorian Bailey
#Section 0003
#Program 10
#Created on November 9th 2021 
#Due November 12th 2021
def openfile():
    '''opens the file and makes it a list'''
    checker2 = -1
    while checker2 == -1:
        try:
            inputFile = input('Enter the name of the file to open ==>')
            textFile = open(inputFile)
            checker2 = 0
        except IOError:
            print('Could not open file {}'.format(inputFile))
            print('Please Try Again\n')
            checker2 = -1
        if checker2 == 0:
            try:
                line = textFile.readlines()
                checker2 = 0
                return line
            except:
                print('File Not Found')
                checker2 = -1


def remove_punc(string):
    '''removes punctuation from list'''
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string


def output_of_file(x):
    '''outputs the files content and sorts through it'''
    print('\nMost frequently used words')
    print('#'.center(2),'Word'.center(25),'Freq.'.center(25))
    print('='*44)
    set_x = set()
    new_x = []
    word1 = 0
    new_d = {}
    for a in x:
        blah = a.split()
        bleh = blah[:]
        for b in bleh:
            if len(b) > 3:
                set_x.add(remove_punc(b.lower()))
                new_x.append(remove_punc(b.lower()))
    for word in new_x:
        if new_x.count(word) == 1:
            word1 +=1
    u_words = len(set_x)
    for ikey in set_x:
        new_d[ikey] = new_x.count(ikey)
    count = 1
    sorted_dict = {}
    sorted_values = sorted(new_d.values(),reverse=True)
    for i in sorted_values:
        for k in new_d.keys():
            if new_d[k] == i:
                sorted_dict[k] = new_d[k]
    for k,v in sorted_dict.items():
        if count < 11:
            print('{} {} {}'.format(str(count).center(2), k.center(25), str(v).center(25)))
            count += 1
    print()
    print('There are {} words that occur only once'.format(word1))
    print('There are {} unique words in the document'.format(u_words))



output_of_file(openfile())