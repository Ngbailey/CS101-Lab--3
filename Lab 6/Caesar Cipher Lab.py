
checker = -1
while checker == -1:
    checker2 = -1
    while checker2 == -1:
        print('MAIN MENU:')
        print('1) Encode a string')
        print('2) Decode a string')
        print('Q) Quit')
        userMenu = input('Enter your selection ==>')
        print()
        if userMenu == '1':
            checker2 = 0
            encode = input('Enter (brief) text to encrypt:')
            encodechecker = -1
            while encodechecker == -1:
                if encode.isdigit() is True:
                    print('please do not enter integers.')
                    encode = input('Enter (brief) text to encrypt:')
                else:
                    encodechecker = 0
                    break 
            encode1 = encode.upper()
            shift1 = int(input('Enter the number to shift letters by: '))
            print('Encrypted: ',end='')
            for i in encode1:
                if i == ' ':
                    print(" ",end='')
                    continue
                i = ord(i)
                i += shift1
                newi = chr(i)
                print(newi, end='')
            print()
            print()
        elif userMenu == '2':
            decode = input('Enter (brief) text to decrypt: ')
            decodechecker = -1
            while decodechecker == -1:
                if decode.isdigit() is True:
                    print('please do not enter integers.')
                    decode = input('Enter (brief) text to decrypt:')
                else:
                    decodechecker = 0
                    break
            checker2 = 0
            decode1 = decode.upper()
            shift1 = int(input('Enter the number to shift letters by: '))
            print('Decrypted: ',end='')
            for i in decode1:
                if i == ' ':
                    print(" ",end='')
                    continue
                i = ord(i)
                i -= shift1
                newi = chr(i)
                print(newi, end='')
            print()
            print()
        elif userMenu == 'Q' or userMenu == 'q':
            checker2 = 0
            checker = 0
            break
#finished