"""
Write a Python program that, given a positive integer num by user input, 
computes its reverse (the number with the digits by the reverse order) and prints it.

You are not allowed to use string manipulation (for example string concatenation).

For example:

for num=766, the output is 667
for num=789, the output is 987
for num=45654, the output is 45654
"""
num = int(input())
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)