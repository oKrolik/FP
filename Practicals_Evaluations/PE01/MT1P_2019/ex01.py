n = int(input())
aux = n
digit = rev = 0
while (aux > 0):
    digit = aux % 10
    rev = rev * 10 + digit
    aux //= 10
print(rev)