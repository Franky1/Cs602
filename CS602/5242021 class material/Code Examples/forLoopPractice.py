''' Practice problems on for loops from Handout 4 '''

#  LOOP variable IS NOT local to the loop - it remains visible after it 
#    and has the value that its *last value inside the loop*
# for i in 'abc':
#     print (i)
# print(i)        

'''
Print every second word in a sentence inputted by the user.
'''
# sentence = " TOday is a bright sunny day. "
# words = sentence.split();
# 
# for pos in range(1, len(words), 2)  :
#     #print(words, 'pos = ', pos)
#     print (words[pos])

# Can also do it using list splicing:
sentence = " TOday is a bright sunny day. "
for word in  sentence.split()[1::2]:
   print (word)


'''
'2. Print all Olympic years in the 21st century, including a designation of which
games (winter or summer) will be conducted.
'''
print ('Method 1:') 
for year  in range(2000, 2100, 2):
    print (year, 'summer' if year % 4 == 0 else 'winter' )
 
# Other methods of doing the same thing
#     
# for year  in range(2000, 2100, 2):
#     if year in range(2000, 2100, 4):
#             print (year, 'summer')
#     else: print (year, 'winter') 


# for year  in range(2000, 2100, 2):
#     if year % 4 == 0 :
#             print (year, 'summer')
#     else: print (year, 'winter')     
# 

# 
# i = 1
# for olym in range(2000, 2100, 2):
#     print(i, end = ' ')
#     if i % 2 == 1:
#         print (olym, 'summer')
#     else: 
#         print (olym, 'winter')
#     i += 1


''''
3. Print the following table: each row from (1 to 25) must contain numbers in the
range between 0 and 25, divisible by the row number. 
'''
for row in range (1, 26):
    print ('\n ' , row, end = ' :')
    # print all multipes of row from 0 to 25
    for num in range (0, 26, row):
        print (num, end = ' ')

#  The following also works, but does not take advantage from
#       python's useful features
# 
# for row in range (1, 26):
#     print (row, end = ' :')
#     # print all multipes of row from 0 to 25
#     line = ''
#     for num in range(0, 26):
#         if (num % row == 0):
#             line = line + (' ' + str(num))
#     print (line)
#     

