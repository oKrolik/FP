"""
Write a Python script that reads two integers, representing the hours (in the interval [0, 24[) 
and minutes (in the interval [0, 60[), using the 24-hour format and prints the equivalent hour in the 12-hour format.

The 12-hour clock is a time convention in which the 24 hours of the day are divided into two periods, 
"am" and "pm", each of 12 hours, numbered: 12 (acting as 0), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 11
(https://en.wikipedia.org/wiki/12-hour_clock).

The minutes are always represented with two digits and, If the minutes' value is zero, 
it should not appear in the output (see the examples).

If the hours and minutes values are incorrect, the script must print the message 
"INVALID DATE FORMAT".

IN:
17
8
OUT:
5:08 pm
"""
from time import gmtime, strftime

h = int(input())
m = int(input())

if (h >= 24 or m >= 60):
    print("INVALID DATE FORMAT")
else:
    if (h == 0):
        if (m == 0):
            print("12 am")
        else:
            print(strftime('12:%M am', gmtime(m*60)))
    else:
        if (h < 12):
            if (m == 0):
                print(f"{h} am")
            else:
                print(strftime(f'{h}:%M am', gmtime(m*60)))
        elif (h > 12):
            if (m == 0):
                print(f"{h%12} pm")
            else:
                print(strftime(f'{h%12}:%M pm', gmtime(m*60)))
        else:
            if (m == 0):
                print("12 pm")
            else:
                print(strftime('12:%M pm', gmtime(m*60)))


#print(strftime(f'{h%12}:%M {time}', gmtime(m*60)))

