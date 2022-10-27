"""
Write a Python program that, given an integer, by user input, between 1 and 10,
prints a pattern on the console, as in the following examples:

If number = 5:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""


n = int(input())

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()