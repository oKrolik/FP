"""
Write a Python program that asks the user to input a positive 4-digit number n and prints the numbers that compose its expanded form.

For example, the expanded form of 1543 is 1000+500+40+3. The expected output for a user input of 1543 is

1000
500
40
3
"""
n = int(input())
print(n//1000*1000)
print((n//100)%10*100)
print((n//10)%10*10)
print(n%10*1)