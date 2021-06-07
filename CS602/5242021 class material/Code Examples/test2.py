#while loop
from dask.array.random import random
print('#1')    
count = 0
while count < 5:
    print(count,"is less then 5")
    count = count + 1
else:
    print(str(count) + " is not less then 5")    
print('='*50)   

print('#2') 
from _ast import Continue
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print('='*50)

print('#3') 
i = 0
while i < 6:
    i += 1
    if i == 3:
        Continue
    print(i)

print('='*50)

#for loop
print('#4')
fruits = ["apple", "banana","cherry"] # a list
for x in fruits:
    print(x)
print('='*50)

for x in "banana":
    print(x)
print('='*50)

for x in range(6):
    print(x)
print('='*50)

for x in range(2,6):
    print(x)    
print('='*50) 
print()
print()

