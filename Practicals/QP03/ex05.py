"""
Write a Python script that, given two numbers n1 and n2 provided by the user,
produces a new number result by joining the last digit of n1 (i.e. the least significant)
with the last digit of n2, and so on for the other digits.

The number of digits of n1 and n2 is the same.

For example:

if the numbers given are n1=123 and n2=456, the resulting number is 362514.
"""

num1 = int(input())
num2 = int(input())
rev1 = rev2 = 0
while num1 > 0:
    resto1 = num1 % 10
    resto2 = num2 % 10
    rev1 = rev2 * 10 + resto1
    rev2 = rev1 * 10 + resto2
    num1 //= 10
    num2 //= 10
print(rev2)