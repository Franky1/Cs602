'''
Created on May 28, 2021
@author: ruded
'''
# Write a code segment that prints out all characters of a string one character per line in
# reverse, from last one to the first one.
# First Example
inputString = input('Enter a string: ')
for i in range(len(inputString) - 1, -1, -1):
    print(inputString[i])

# Second Example
# str = "abcde"
# pos = len(str)-1 #will be used to refer to the position within str
# while pos >= 0 :
#     print( str[pos] )
#     pos -= 1

# Third Example
# str = "abcde"
# pos = 1 #will be used to refer to the position within str
#         #  0, 1, 2....len(str)-1
# while pos <= len(str) :
#     print( str[-pos] )
#     pos += 1
