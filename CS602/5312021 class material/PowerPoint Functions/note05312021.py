"""
globalVar = 1

def f1():
      localVar = 2
      print(globalVar)
      print(localVar)

f1()
print(globalVar)
#2
x = 1

def f1():
    x = 2
    print(x) # Displays the value 2

f1()
print(x) 

#3
x = eval(input('Enter a number: ')) 
if x > 0:
     y = 4
else:
     y=3

print(y) 

#4
sum = 0
for i in range(5):
     sum += 1

print(sum)

#5
x = 1
def increase():
      global x
      x += 1
      print(x)

print(x)
increase()

#6
def printArea(width = 1, height = 2):
       area = width * height
       print(area)

printArea()
printArea(4, 2.5)
printArea(height = 5, width = 3)
printArea(width = 1.2)
printArea(height = 6.2)

#7
def sort(num1, num2):
      if num1 < num2:
           return num1, num2
      else:
           return num2, num1

n1, n2 = sort(3, 2) 
print('n1 is ', n1)
print('n2 is ', n2)

#8
def f(x, y):
      return x + y, x - y, x * y, x / y

t1, t2, t3, t4 = f(9, 5) 
print(t1, t2, t3, t4)


a = 0
b = 1
for i in range(10):
     a += b
     b += 1
print(a)

donuts = int(input("How many donuts? "))

dozens = int(donuts/12)
leftover= donuts%12
if leftover == 0:
    print( f'{donuts} donuts is {dozens} dozen donuts.' )
else:
    print( f'{donuts} donuts is {dozens} dozen and {leftover} donuts.' )

a = 1
print(f"{f'{a:03}':>6}")
    

import requests
if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    print(req.text)

print(max(1, 2),min(1,2))
print(max([1,2]))
print(max((1,2)))
"""

import time
  
print('Enter to start, Ctrl + C to stop。')
while True:
    
    input("") 
    starttime = time.time()
    print('start')
    try:
        while True:
            print('timmer: ', round(time.time() - starttime, 0), 'second', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('end')
        endtime = time.time()
        print('total time:', round(endtime - starttime, 4),'secs')
        break