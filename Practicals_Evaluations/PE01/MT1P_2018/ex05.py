"""
dec = int(input())
print(oct(dec)[2:])
"""

dec = int(input())
oct = place = 0
aux = dec
while aux:
    oct = aux % 8 * 10 ** place + oct
    aux //= 8
    place += 1
print(oct)