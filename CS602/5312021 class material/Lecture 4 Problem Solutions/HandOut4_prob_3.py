'''
Created on May 28, 2021
@author: ruded
'''
value = 1
count = 0
while value % 2 != 0:
    value = eval(input('Enter a value: '))
    count += 1
print(f'{count - 1} odd values were input.')

# num = int(input('please enter an even number'))
# num = 1
# while num % 2 != 0:
#    num = int(input('please enter an even number'))
