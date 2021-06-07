'''Created on Aug 27, 2018 @author: DRUDE
Demo of built-in types'''
# numeric types: int, float, complex
print (3, 'has type', type(3))
print (-4.5 , 'has type', type(-4.5))
print (complex(3,4), 'has type', type ( complex(3,4) ))
# have no range limit
a = 30000000000000000000000000000+1
print (a, 'has type', type(a))
print (1/a, 'has type' , type(1/a))
print ('\nStrings ----------------------------------------------------')
# str type
print (type('abc'))
print (type('a'))
print (type("also a string"))
print ('\nSequences ------------------------------------------------')
# sequence types: list, tuple range
lst = [a, 'b', 4.3, -9]
lst [3] = 55 #lists are mutable, i.e. can be changed
print (lst, ' has type ', type(lst))
tpl = (3, 7 , 'foo')
print (tpl, ' has type ', type(tpl))
r = range(20, 30, 2)
print(r, ' has type ', type(r))