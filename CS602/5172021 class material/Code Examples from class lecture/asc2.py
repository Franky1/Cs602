'''
Created on May 16, 2021
@author: ruded
'''
'''
Big long string of all the different characters
'''
charString = '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}~'
print('(Character) ASCii-Value')

# Get the length of the big string
stringLen = len(charString)
counter = 0  # counter to keep track of items printed on an output line
for i in range(stringLen):
    if counter > 15:
        counter = 0
        print()
    else:
        # an example of using the ord method to get the integer value of a character
        print(f'({charString[i]}) {ord(charString[i]):<3}', end='| ')
        counter += 1
print('(")', ord('"'), end='| ')        
print("(')", ord("'"))

print()
print('ASCii-Value (Character)')

counter = 0
for i in range(33, 127):
    if counter > 15:
        counter = 0
        # example of using the char method to get the character based on an integer value
        print(f'{i} ({chr(i)})', end='| ')
        print()
    else:
        # example of using the char method to get the character based on an integer value
        print(f'{i} ({chr(i)})', end='| ')
        counter += 1
print(); print()   
charValue = input('Enter a single character: ')
integerValue = eval(input('Enter a integer value in the range of 33 - 126 inclusive: '))

print(f'The character value you entered, {charValue}, is the ASCii value {ord(charValue)}.')
print(f'The integer value you entered, {integerValue}, is the character value {chr(integerValue)}.')

