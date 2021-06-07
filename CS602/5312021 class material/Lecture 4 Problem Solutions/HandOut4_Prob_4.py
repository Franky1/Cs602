'''
Created on May 28, 2021
@author: ruded
'''
# 4. Write a code segment that gives the user 5 attempts at entering 
# a word with at least 7 characters. Stops the loop after the entered
# word is 7 chars or longer, or after 5 attempts were exhausted.

word = input('please enter a word with at least 7 chars')
attempts = 1
while len(word) < 7 and attempts <= 4:
     word = input('please enter a word with at least 7 chars')
     attempts += 1
