##Name: Thiago Bardini
##CIT125 Python Programming
##Spring 2020
##Project 1: Caesar Cipher

choice=''
print('Please enter your choice ')

while True:
    print('\'e\' to encode a string')
    print('\'d\' to dencode a string')
    print('\'q\' to quit a string')
    choice=input().lower()

    if choice=='e':
        text=input('Enter a string to encode: ')
        rotation=0
        while True:
            rotation=int(input('Enter a rotation between 1-25: '))
            if 1<=rotation and rotation<=25:
                break
            else:
                print('Rotation key should be between [1-25]')
        encoded_text=''
        for letter in text:
            if 97<=ord(letter) and ord(letter)<=122:
                num=97+ (ord(letter)-97 + rotation)%26
                encoded_text+=chr(num)
            else:
                encoded_text+=letter
        print('Encoded text',encoded_text)

    elif choice=='d':
        text=input('Enter a string to decode: ')
        rotation=0
        while True:
            rotation=int(input('Enter a rotation between 1-25: '))
            if 1<=rotation and rotation<=25:
                break
            else:
                print('Rotation key should be between [1-25]')
        decoded_text=''
        for letter in text:
            if 97<=ord(letter) and ord(letter)<=122:
                num=97+ (ord(letter)-97 - rotation)%26
                decoded_text+=chr(num)
            else:
                decoded_text+=letter
        print('Decoded text',decoded_text)

    elif choice=='q':
        print('Thank you !')
        break

    else:
        print('Invalid input. Try again!')
