'''
Created on Oct 7, 2020
@author: ruded
'''

def sum(num1, num2):
    result = 0
    for i in range(num1, num2 + 1):
        result += i
        
    return result

def main():
    print('Sum from 1 to 10 is', sum(1,10))     # call the sum function
    print('Sum from 20 to 37 is', sum(20,37))   # call the sum function
    print('Sum from 35 to 49 is', sum(35,49))   # call the sum function
    
main() # call the main function