"""
The octal numeral system uses digits from  to  ( to  in binary) to 
represent a number (more info).

Write a python program that takes in a number in the octal system 
and converts it into decimal.

If the number is not octal, print the message 'Not a valid number.'
"""

octal = input()
value = 0
aux = int(octal)
flag = True
while aux:
    digit = aux % 10
    if digit > 7:
        print("Not a valid number.")
        flag = False
        break
    aux //= 10
if flag:
    for i in range(len(octal)):
        value = value * 8 + int(octal[i])
    print(value)