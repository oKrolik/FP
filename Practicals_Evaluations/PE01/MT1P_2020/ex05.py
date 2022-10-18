from re import I


a = int(input("a? "))
b = int(input("b? "))

i = a

while (i < b and not(i**2 > (b/2)**2)):
    n = i
    if not(i % 3 == 0 and i % 5 == 0):
        if (i % 2 == 0):
            n //= 2
            n //= 2
            n //= 2
        if not(i % 2 == 0):
            n += 1
        print(n)
    i += 3