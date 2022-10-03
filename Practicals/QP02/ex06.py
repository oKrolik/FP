"""
The formula for computing the final amount if one is earning compound interest is given on Wikipedia as:

A=P*(1+r/n)**(nt)

where:

P = principal amount (the amount that the interest is provided on)
r = the interest rate
n = the frequency that the interest is paid out (per year)
t = the number of years that the interest is calculated for

Use Spyder to write a program that replaces these letters with something a bit more human-readable and calculate the
final amount (A) at the end of the second year, for some varying amounts of money (P), payment frequency (n) at
realistic interest rates (r).

Please round the result for 3 digits using round().

For example:

for P = 1000, r = 1% and n = 2 the result is 1020.151
for P = 650, r = -0.05% and n = 1 and the result is 649.35
"""
p = int(input())
r = float(input())
n = float(input())
print(round((p*(1+(r/n))**(n*2)), 3))