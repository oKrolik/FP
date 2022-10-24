"""
Write a Python program that takes an integer num, 
any integer provided by the user, and outputs the multiplication table with lines: 
num x index = res, where res = num * index and index is a number that goes 
from 1 to a maximum of 10.

When the number is multiplying by itself, 
the displayed format should be num ^ 2 = res and nothing else is added to the output.

For example for num = 5 the output is:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 ^ 2 = 25
"""

n = int(input())
for i in range(1, 11):
    if (i == n):
        print(f"{n} ^ 2 = {n*i}")
        break
    print(f"{n} x {i} = {n*i}")