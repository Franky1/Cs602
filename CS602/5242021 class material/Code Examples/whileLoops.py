'''
Created on Sep 13, 2018

@author: AACPOD
'''
# 1  print  out all characters of a string one character per line in
# reverse, from last one to the first one.
# '''Start at the end of the string 
# REPEAT while have not reached the beginning:
#     print one char
# '''
# str = "abcde"
# pos = len(str)-1 #will be used to refer to the position within str
# while pos >= 0 :
#     print( str[pos] )
#     pos -= 1

# str = "abcde"
# pos = 1 #will be used to refer to the position within str
#         #  0, 1, 2....len(str)-1
# while pos <= len(str) :
#     print( str[-pos] )
#     pos += 1

# 2. Write a code segment that allows the user to enter 10 numbers and
# computes and prints #out their sum, average, product.
# '''
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

# # 3. Read input until user enters an even number.
# #num = int(input('please enter an even number'))
# num = 1
# while num % 2 != 0:
#     num = int(input('please enter an even number'))


# 4. Write a code segment that gives the user 5 attempts at entering 
# a word with at least 7 characters. Stops the loop after the entered
# word is 7 chars or longer, or after 5 attempts were exhausted.

word =  input('please enter a word with at least 7 chars')
attempts = 1
while len(word) < 7 and attempts <= 4:
     word =  input('please enter a word with at least 7 chars')
     attempts += 1




#5. Write a code segment that keeps reading words, so long that 
# they appear in alphabetical order. Once the order is violated, 
#stop and print out how many words started with a vowel.


startWithVowel = 0

previous = ''
current = input("Enter word:")

if current[0].upper() in 'AEIOUY':
    startWithVowel += 1
    print (current , 'starts with a vowel')
    
while previous.lower() <= current.lower() :
        
    previous = current
    #read another word
    current = input("Enter word:")
    if current[0].upper() in 'AEIOUY':
        startWithVowel += 1
        print (current , 'starts with a vowel')
    
print ('startWithVowel = ', startWithVowel)



#calculate a sum, product, average of 10 numbers from user

# i = 1 # counter
# sum = 0
# prod = 1
# numNumbers = 3
# while i <= numNumbers:
#     num = eval(input('enter next number'))
#     sum += num
#     prod *=num
#     
#     i+= 1
#     
# print (sum, 'ave ',  sum/numNumbers)

    
