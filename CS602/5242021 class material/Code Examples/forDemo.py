''' Demo of a for loop '''


# for ch in "bentley":
#     print(ch)
#  
# for var in range(1,101):
#     print(var, end = " ")
    
# var = 1;
# while var <= 100:
#     print (var)   
#     var += 1
#   

# line = input("Please enter a sentence and I will output the words \
# in the sentence, which are longer than 3 characters long\n")
# for word in line.split():
#     if (len(word) > 3) :
#         print(word)
       

# line = "bentley"
# for ch in line:
#     line = 'foo'
#     print(ch)
    
# GIVEN A STRING, PRINT ONLY THE FIRST 3 LETTER OG THE STRING

# for i in range(0,3):
#     print (line[i])
# 
# for ch in line[0:3] :
#     print (ch)
#  


#
#  BAD STYLE - using BREAK AND CONTINUE
#    
#  SHOULD BE AVOIDED by using CONDITIONALS instead
# 
#
line = 'september'

for i in range (0, len(line)):
    print (i)
    if (i == 3): 
        continue
    print (line[i])

print ('done')

# for i in range (0, len(line)):
#     if (i == 3): 
#         break
#     print (line[i])
# 
# print ('done')


#     
    



 