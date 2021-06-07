'''
Created on Sep 24, 2018
Demo of function definitions
@author: TBABAIAN
'''


def parseHourMinSec (strTimeHM, separator = ':', seconds = False ):
    print ('parsing ', strTimeHM, end = " --> ")
    if seconds:
        h, m, s = strTimeHM.split(separator)
    else:  
        h , m  = strTimeHM.split(separator); s = 0
    
    print (' h = ', h, 'm = ', m, 's = ', s)

    return h, m, s

def main(x):
    print (parseHourMinSec('6:22'))
    print (parseHourMinSec('12.00.10', '.', True))
    
    hour, min, sec = parseHourMinSec('12:33:45', seconds = True)
    print (' hour = ', hour, 'min = ', min, 'sec = ', sec)


main('x')