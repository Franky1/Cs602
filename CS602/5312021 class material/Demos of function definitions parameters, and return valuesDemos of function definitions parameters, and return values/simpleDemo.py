'''
Created on Sep 25, 2018
Simplest function definition and function calls
@author: root
'''

# 
# # The following is a function definition
# # This function has no parameters and no return value 
# def printHelloWorld():
#     print ('Hello, world')
#      
#      
#  # call the above function three times 
# printHelloWorld()
# printHelloWorld()
# printHelloWorld()
    
 
#---------------------------------------------
# Function takes a single parameter; returns no value
# def printHello (name):    
#     print ('Hello,' , name , '!')
# 
#       
#         
# printHello('Tamara')
# 
# aname = input('Greetings! what is your name?')
# printHello(aname)
# print(aname)
#   
#  
# #--------------------------------------------------------
# # Function takes a single parameter, returns a single value
# 
def helloString (name = 'David'):
    result = 'Hello, ' + name + '!'
    return result
 
greetingString =  helloString('Cathy')
print(greetingString)
# 
# 


