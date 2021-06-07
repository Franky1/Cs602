'''
Created on May 28, 2021
@author: ruded
'''
# 5. Write a code segment that keeps reading words, so long that 
# they appear in alphabetical order. Once the order is violated, 
# stop and print out how many words started with a vowel.

startWithVowel = 0

previous = ''
current = input("Enter word:")

if current[0].upper() in 'AEIOUY':
    startWithVowel += 1
    print (current , 'starts with a vowel')
    
while previous.lower() <= current.lower():
        
    previous = current
    # read another word
    current = input("Enter word:")
    if current[0].upper() in 'AEIOUY':
        startWithVowel += 1
        print (current , 'starts with a vowel')
    
print ('startWithVowel = ', startWithVowel)
