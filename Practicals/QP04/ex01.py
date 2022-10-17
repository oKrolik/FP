"""
Write a Python Boolean function calc_triangular(n) 
that receives a positive integer n and calculates the nth triangular number.
The nth triangular number (Tn) is the number of dots in the triangular arrangement 
with n dots on each side, and is equal to the sum of the n natural numbers from 1 to n
(https://en.wikipedia.org/wiki/Triangular_number):
 
    n
Tn=∑    k = 1 + 2 + 3 + … + n
    k=1

For example:
t1 = 1
t2 = 3
t3 = 6
t4 = 10
"""

def calc_triangular(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
    
"""
print("calc_triangular(1)")
print(calc_triangular(1))
print("calc_triangular(3)")
print(calc_triangular(3))
print("calc_triangular(10)")
print(calc_triangular(10))
print("calc_triangular(23)")
print(calc_triangular(23))
"""