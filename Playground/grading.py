"""
Write a Python program that, given the four components of the FP final grade,
by user input, returns the student's grade, an integer from 0 to 20, by using the formula:

grade = (LE + RE + 13 * PE + 5 * TE) / 100

The program returns:

"Input error", if the any of the components is not between 0 and 100
"RFF", if the PE < 40 or the TE < 40
the grade as an integer, otherwise
Careful: There are many ways to round a number. You may want to avoid using round() 
since it uses "round half to even" but grades are rounded using "round half up". 
"""
from math import floor

le = int(input())
re = int(input())
pe = int(input())
te = int(input())
if ((le < 0 or le > 100) or (re < 0 or re > 100) or (pe < 0 or pe > 100) or (te < 0 or te > 100)):
    print("Input error")
elif (pe < 40 or te < 40):
    print("RFF")
else:
    print(floor((le+re+13*pe+5*te)/100+0.5))