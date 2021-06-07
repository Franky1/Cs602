'''
Created on May 28, 2021
Demo of function definitions
@author: DRUDE
'''

            
def toMin (strTimeHM, sep = ':'):
    ''' 
    Parameters:
       strTimeHM - a string of format 'HH:MM', where HH is hour, MM is minute.    
    Returns a single integer corresponding to the time specified by 
            the parameter, converted to minutes. 
    '''
    h , m = strTimeHM.split(sep)
    print (' h = ', h, 'm = ', m)
    minutes = int(h)*60 + int(m)
  
    return minutes

def main():
    min = toMin('15:00')
    print (min)

    print (toMin('6:22'))
    print (toMin('6:00'))
    
    print(toMin('14.15', '.'))

    timeEntry = input('Please enter time, e.g. 7:23 or 11.05')
    print (toMin(timeEntry))

main()

