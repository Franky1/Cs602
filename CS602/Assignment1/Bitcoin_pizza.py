#Qiaofei Yan
#Assignment1-Cs602

import math
#BTC10 is 2010 bitcoin price,
BTC10 = 0.0041
#BTC21 is 2021 USD price,
BTC21 = 57124.90
#BTC21_E is 2021 EUROS price,
BTC21_E = 47800.54
#PIZZA_SIZE is 16 inch so the radius will be 16/2
PIZZA_R = 16/2


#The cost of Laszlo's pizza in 2010, in USD 
PIZZA_2010 =  BTC10*10000
# The cost per bite of his pizza in 2010. 
# The area of the pizza, rounded to three decimal places 
S = math.pi * PIZZA_R* PIZZA_R
Pizza_bit_price_10 = PIZZA_2010/S
# The value of his purchase today in USD, had he invested the BTC instead. 
PIZZA_2021 = BTC21*10000
# The cost per bite in 2010 and 2021. 
PIZZA_bit_price_21 = round(PIZZA_2021/S,2)
# The percentage increase of bitcoin from 2010 to 2021.
Percentage = (PIZZA_2021 - PIZZA_2010)/PIZZA_2010

#output
print("This Program Calculates:")
print("\t- cost of the first pizza purchased with bitcoin, then and now"'\n'
      "\t- cost of one bite of pizza, then and now, and its area "'\n'
      "\t- percentage increase in bitcoin from 2010 to 2021."'\n'
      "\t- values of bitcoin purchases then and now")
print()

#Ask user name
name = input('What is your name? ' )
print(f"Happy Bitcoin Pizza Day, {name.upper()}!")
print(f"Laszlo's pizza cost 10000 BTC, or ${PIZZA_2010:,.2f} in 2010.")
print(f"Today 10000 BTC is worth $ {PIZZA_2021:,.2f}.")
print(f"The area of the pizza is {S:.3f} square inches.")
print(f"The cost of one bite of pizza in 2010 was ${Pizza_bit_price_10:,.2f}")
print(f"That would be ${PIZZA_bit_price_21:,.2f} in 2021.")
print(f"Bitcoin has increased in value by {Percentage:,.2f}% from 2010 to 2021.")
print("="*50)
print()

#Ask user amount
Btc1 = eval(input(name + \
', How many dollars would you like to invest in bitcoin? '))
BTC_Price_10 = Btc1 / BTC10
BTC_Price_20 = Btc1 / BTC21
BTC_Price_20_E = BTC_Price_20 * BTC21_E

print(f"${Btc1:,.2f} Would have purchased {BTC_Price_10:.6f} BTC in 2010.")
print(f"${Btc1:,.2f} will purchase {BTC_Price_20:,.6f} BTC today.")
print(f"Today {BTC_Price_20:,.6f} BTC is worth {BTC_Price_20_E:,.2f} EURO.")