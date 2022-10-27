"""
Write a Python function C that receives the number of objects to choose from n, 
the number of objects selected r and produces all combinations possible.

Round the result to the floor, for example the floor of 8.4 is 8 and the floor 
of 5.7 is 5. 

You cannot use the math package.
"""

def my_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * my_factorial(n-1)

def c(n, r):
    return (my_factorial(n)/(my_factorial(r)*my_factorial(n-r)))