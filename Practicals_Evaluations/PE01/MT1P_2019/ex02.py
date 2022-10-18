d = int(input())
num = int(input())
aux = num
sum = 0
while (aux > 0):
    digit = aux % 10
    if (digit > d):
        sum += digit**2
    aux //= 10
print(sum)