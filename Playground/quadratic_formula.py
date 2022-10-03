"""
Write a Python program that takes in three integers a, b, c of the
formula by user input and prints the solutions to the console.
Please use round() with two decimal places.

For example:

a = 2, b = 3, c = -5, it should print "The solutions are -2.5 and 1.0"
Please note: assume the inputs are always valid and will result in real integer
or float numbers and never imaginary numbers or impossible results.

Hint:

The expression for the quadratic formula is: ax^2+bx+c = 0, where ,  and  will be given by user input.
Don’t forget to “import math” in the beginning of your program.
You can see all math python functions in here: https://docs.python.org/3/library/math.html
"""
from math import sqrt
a = int(input())
b = int(input())
c = int(input())
print("The solutions are {} and {}".format(round((-b + sqrt((b**2)-4*a*c))/(2*a),2), round((-b - sqrt((b**2)-4*a*c))/(2*a),2)))