'''
Created on May 30, 2021
@author: ruded
Program: printCalendarStub
'''


# stub for printMonth
def printMonth(year, month):
    print('In printMonth')
    print('-------------')
    print('-> Calling printMonthTitle'); printMonthTitle(year, month)
    print('-> Calling printMonthBody'); printMonthBody(year, month)
    print('<- Existing printMonth')


# stub for readInput
def readInput():
    print('In readInput')
    print('------------')
    year = eval(input('Enter full year (e.g. 2021): '))
    month = eval(input(
         'Enter month as a number between 1 and 12: '))
    print('<- Exiting readInput')
    return year, month


# stub for printMonthTitle
def printMonthTitle(year, month):
    print('In printMonthTitle')
    print('------------------')
    print('-> Calling getMonthName'); getMonthName(month)
    print('<- Exiting printMonthTitle')


# stub for getMonthBody
def printMonthBody(year, month):
    print('In printMonthBody')
    print('-----------------')
    print('-> Calling getStartDay'); getStartDay(year, month)
    print('-> Calling getNumOfDaysInMonth'); getNumOfDaysInMonth(year, month)
    print('<- Exiting printMonthBody')


# stub for getMonthName
def getMonthName(month):
    print('In getMonthName')
    print('---------------')
    print('<- Exiting getMonthName')


# stub for getStartDay
def getStartDay(year, month):
    print('In getStartDay')
    print('--------------')
    print('-> Calling getTotalNumOfDays'); getTotalNumOfDays(year, month)
    print('<- Exiting getStartDay')


# stub for getTotalNumOfDays
def getTotalNumOfDays(year, month):
    print('In getTotalNumOfDays')
    print('--------------------')
    print('-> Calling isLeapYear'); isLeapYear(year)
    print('-> Calling getNumOfDaysInMonth'); getNumOfDaysInMonth(year, month)
    print('<- Exiting getTotalNumOfDays')


# stub for getNumOfDaysInMonth
def getNumOfDaysInMonth(year, month):
    print('In getNumOfDaysInMonth')
    print('----------------------')
    print('-> Calling isLeapYear'); isLeapYear(year)
    print('<- Exiting getNumOfDaysInMonth')


# stub for isLeapYear
def isLeapYear(year):
    print('In isLeapYear')
    print('----------')
    print('<- Exiting isLeapYear')


# stub for main
def main():
    print('In main function')
    print('-------------')
    print('-> Calling readInput'); y, m = readInput()
    print('-> Calling printMonth'); printMonth(y, m)
    print('<- Exiting main')


main()

