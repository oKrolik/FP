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

num = int(input())
if num > 0:
    limit = 10 if num > 10 else num
    for i in range(1,limit+1):
        if (i == num): print(f"{num} ^ 2 = {num*i}")
        else: print(f"{num} x {i} = {num*i}")
else:
    limit = 10
    for i in range(1,limit+1): print(f"{num} x {i} = {num*i}")