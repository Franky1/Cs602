'''
Created on Jan 13, 2020 by drude
Simple example program for the first class.
Converts temperature in degrees Fahrenheit to Celsius according to the formula
TC = (TF -32)* 5/9
'''
print ('This program converts temperature in degrees Fahrenheit to degrees Celcius')
fahStr = input('Please enter an integer number of degrees F ')
fah = eval(fahStr) # evaluate the string, will convert input string into a number 
celcius = (fah - 32) * 5 / 9
print (fah, 'degrees F equals ', celcius, ' degrees C')