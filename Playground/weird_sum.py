"""
Write a Python script that, given two integers a and b, prints the value of their sum.

- However, if the difference of a and b is an even number, the value of the sum is doubled.
- On the other hand, if the difference is an odd number, 
the value of the product of a and b gets added to the value of the sum.
Do not use conditionals (e.g., if or while).
"""

# cyclomatic complexity is 3
a = int(input())
b = int(input())
print((a-b)%2==0 and 2*(a+b) or a*b+a+b)

"""
# cyclomatic complexity is 1
a=int(input())
b=int(input())
t=(a-b)%2==0
print((a+b+a*b)*(not t) + ((a+b)*2)*t)
"""