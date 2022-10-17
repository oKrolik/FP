"""
Write a Python function deriv(f) that receives a function f and returns a new function that 
computes df(x) numerically using the approximation below. Use round to approximate the result to 3 decimal places.

Recall that the derivative df(x) of a real function f(x) is defined as a limit:

df(x)=limh→0f(x+h)-f(x)h

For a small h, we can numerically compute the derivative using the equation:

df(x)=f(x+h)-f(x)h,

For the sake of simplicity, consider h=0.001.      
"""

#import math

def deriv(f):
    def df(x, h=0.001):
        return round((f(x+h) - f(x)) / h,3)
    return df

"""
def f1(x):
    return x*x + 2*x + 2
print(deriv(f1)(3))

def f2(x):
    return math.sin(x) / x
print(deriv(f2)(3.14))

def f3(x):
    return math.log(x+10)
print(deriv(f3)(-5))

def f4(x):
    return 3/x + 5
print(deriv(f4)(55.231))
"""