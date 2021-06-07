'''
Created on May 28, 2021

@author: ruded
'''
# Write a code segment that allows the user to enter 10 numbers and computes and prints
# out their sum, average, product.
totalSum = 0
totalProduct = 1
totalAverage = 0
for i in range(10):
    value = eval(input(f'Enter number {i + 1}: '))
    totalSum += value
    totalProduct *= value
print(f'Sum : {totalSum}')
print(f'Average: {totalSum / 10}')
print(f'Product: {totalProduct:,}')
    
# REPEAT 10 times
#     read number 
#     update sum
# '''
# i = 0
# sum = 0; product = 1
# limit = 10
# while i < limit:
#     num = eval (input('please enter next num '))
#     sum += num  
#     product *= num
#     i += 1
# print ('sum = ', sum, "prod =", product, 'ave = ' , sum / limit)

# # read a list of 10 numbers in one input
# str= input("enter 4 numbers separated with a space")
# lst = str.split()
# print (lst)
