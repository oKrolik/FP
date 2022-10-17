"""
Write a function compute_euler(n) that given a positive integer n,
computes the approximation of e using the following truncated series sum,
from 0 to n:

e≈∑nk=01k!

where k!=1x2x⋯x(k-1)xk is the factorial of k (see math.factorial).

By taking larger values of n we can obtain better approximations.

Use round to approximate the result to 5 decimal places.
"""

from math import factorial

def compute_euler(n):
    sum = 0
    for i in range(n+1):
        sum += 1/factorial(i)
    return round(sum, 5)

"""
print("compute_euler(50)")
print(compute_euler(50))
print("compute_euler(5)")
print(compute_euler(5))
print("compute_euler(0)")
print(compute_euler(0))
print("compute_euler(1)")
print(compute_euler(1))
"""