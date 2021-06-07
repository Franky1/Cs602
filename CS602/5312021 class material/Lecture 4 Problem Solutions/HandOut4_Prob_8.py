'''
Created on May 28, 2021
@author: ruded
'''
''''
3. Print the following table: each row from (1 to 25) must contain numbers in the
range between 0 and 25, divisible by the row number. 
'''
for row in range (1, 26):
    print ('\n' , row, end=' :')
    # print all multipes of row from 0 to 25
    for num in range (0, 26, row):
        print (num, end=' ')

#  The following also works, but does not take advantage from
#       python's useful features
# 
print('\n')
for row in range (1, 26):
    print (' ' + str(row), end=' :')
    # print all multipes of row from 0 to 25
    line = ''
    for num in range(0, 26):
        if (num % row == 0):
            line = line + (str(num) + ' ')
    print (line)
