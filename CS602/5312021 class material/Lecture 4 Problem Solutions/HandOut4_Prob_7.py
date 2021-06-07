'''
Created on May 28, 2021
@author: ruded
'''
'''
'2. Print all Olympic years in the 21st century, including a designation of which
games (winter or summer) will be conducted.
'''
# print ('Method 1:') 
for year  in range(2000, 2100, 2):
    print (year, 'summer' if year % 4 == 0 else 'winter')
 
# Other methods of doing the same thing
#     
for year  in range(2000, 2100, 2):
    if year in range(2000, 2100, 4):
        print (year, 'summer')
    else: print (year, 'winter') 

# for year  in range(2000, 2100, 2):
#     if year % 4 == 0 :
#             print (year, 'summer')
#     else: print (year, 'winter')     
# 
