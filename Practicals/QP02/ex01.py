"""
Use Spyder to write a program that asks the user to input a digit n (0-9),
calculates the expression n + nn + nnn and prints its value.

For example: for a user input 5, the output must be 5 + 55 + 555 = 615.
"""
n = int(input())
print((n*100+n*10+n)+(n*10+n)+(n))