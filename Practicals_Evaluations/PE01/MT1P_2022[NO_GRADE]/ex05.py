"""
Decimal numbers are base 10 numbers that use only digits from 0 to 9, inclusive.

Senary numbers are base 6 numbers that use only digits 0, 1, 2, 3, 4 and 5.

Write a Python program that converts a senary number (base 6) senary, given by user input, into the corresponding decimal number (base 10).

For example:

for senary=11, the output is the decimal number 7 (because 1*6**1+1*6**0 = 7)
for senary=125, the output is the decimal number 53 (because 1*6**2+2*6**1+3*6**0 = 53)
for senary=1543, the output is the decimal number 423 (because 1*6**3+5*6**2+4*6**1+3*6**0 = 423)
"""

senary = input()
valor = 0
for i in range(len(senary)):
    valor = valor * 6 + int(senary[i])
print(valor)