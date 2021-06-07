'''
Created on May 28, 2021
@author: ruded
'''
'''
Print every second word in a sentence inputted by the user.
'''
sentence = "Today is a bright sunny day. "
print(sentence)
words = sentence.split();
# 
for pos in range(1, len(words), 2):
    # print(words, 'pos = ', pos)
    print (words[pos])

# Can also do it using list splicing:
# sentence = " Today is a bright sunny day. "
# for word in  sentence.split()[1::2]:
#    print (word)
