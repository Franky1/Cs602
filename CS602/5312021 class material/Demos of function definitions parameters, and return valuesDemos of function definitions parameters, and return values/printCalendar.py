'''
Created on May 30, 2021
@author: ruded
Program: printCalendar
'''

# stub for printMonth
def printMonth(year, month):
    printMonthTitle(year, month)
    printMonthBody(year, month)


# stub for readInput
def readInput():
    year = eval(input('Enter full year (e.g. 2021): '))
    month = eval(input(
         'Enter month as a number between 1 and 12: '))
    return year, month


# stub for printMonthTitle
def printMonthTitle(year, month):
    print(f'         {getMonthName(month)} {year}')
    print('-' * 29)
    print(' Sun Mon Tue Wed Thu Fri Sat')


# stub for getMonthBody
def printMonthBody(year, month):
    pass


# stub for getMonthName
def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"
    return monthName


# stub for getStartDay
def getStartDay(year, month):
    pass


# stub for getTotalNumOfDays
def getTotalNumOfDays(year, month):
    pass


# stub for getNumOfDaysInMonth
def getNumOfDaysInMonth(year, month):
    pass


# stub for isLeapYear
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# stub for main
def main():
    y, m = readInput()
    mn = getMonthName(m)
    print('\n', mn, y, '\n')
    print(f'{y} is a Leap year: {isLeapYear(y)}\n')
    printMonth(y, m)


main()




