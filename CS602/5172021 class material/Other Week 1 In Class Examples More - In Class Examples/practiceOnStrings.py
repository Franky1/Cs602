'''
Created on Sep 6, 2018
@author: TBABAIAN
PRactice problems from handout 2 in reverse order
'''

str = 'Brevity is the soul of wit'
words= str.split()
posFSpace = str.find(' ')
posLSpace = str.rfind(" ")
middle = str[posFSpace : posLSpace].strip();
print (words[0].upper() , middle, words[-1].upper())


str = 'blackboard'
posA = str.find('a')
twoLetters = str[posA+1:posA+3].upper()
newstr = str[:posA+1] + twoLetters + str[posA+3:]
print (newstr)


str = "Hi, my name is Tamara"
newstr= str.replace(' ', '-')
print (newstr)


str =  'Some text ( and some more in parens)  is included here. '
posLeft = str.find('(')
posRight = str.find(')')
print (str[posLeft+1:posRight].strip())

str='WooHoo'
print(str[len(str)//2:])

word = 'Bentley'
upperLetters=(word[0]+word[-1]).upper()
print(upperLetters)


str = '9856784433'
phoneWIthDashes = str[:3]+'-'+str[3:6]+'-'+str[6:]
print(phoneWIthDashes)


