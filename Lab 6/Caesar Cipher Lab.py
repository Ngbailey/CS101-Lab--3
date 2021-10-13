def encrypt(encode, shift1):
    encodechecker = -1
    while encodechecker == -1:
        if encode.isdigit() is True:
            print('please do not enter integers in the encryption sequence.')
            encode = input('Enter (brief) text to encrypt:')
        else:
            encodechecker = 0
            break 
    encode1 = encode.upper()
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

def print_Menu():
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

def decrypt(decode, shift1):
    decodechecker = -1
    while decodechecker == -1:
        if decode.isdigit() is True:
            print('please do not enter integers in the decription sequence.')
            decode = input('Enter (brief) text to decrypt:')
        else:
            decodechecker = 0
            break
    decode1 = decode.upper()
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




checker = -1
while checker == -1:
    checker2 = -1
    while checker2 == -1:
        print_Menu()
        userMenu = input('Enter your selection ==>')
        if userMenu == '1':
            encode = input('Enter (brief) text to encrypt:')
            shift1 = int(input('Enter the number to shift letters by: '))
            encrypt(encode, shift1)
        elif userMenu == '2':
            decode = input('Enter (brief) text to decrypt: ')
            shift1 = int(input('Enter the number to shift letters by: '))
            decrypt(decode, shift1)
        elif userMenu == 'Q' or userMenu == 'q':
            checker2 = 0
            checker = 0
            break
        else:
            print('Please enter a value of either 1, 2, or Q/q.')
