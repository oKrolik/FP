"""
Write a Python program that outputs all the prime numbers within a 
closed interval of numbers between lower and upper, given by user input.

For example:

for lower=2 and upper=23 the output is: Prime numbers between 2 and 23 are: 
2 3 5 7 11 13 17 19 23

for lower=5 and upper=27 the output is: Prime numbers between 5 and 27 are: 
5 7 11 13 17 19 23

for lower=-2 and upper=5 the output is: Prime numbers between -2 and 5 are: 
2 3 5
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
print(f"Prime numbers between {a} and {b} are:", end=" ")
for i in range(a, b+1):
    if is_prime(i):
        print(i, end=" ")