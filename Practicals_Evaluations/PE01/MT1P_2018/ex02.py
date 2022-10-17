d = int(input())
num = int(input())
aux = num
sum = 0
while aux > 0:
    digit = aux % 10
    sum += 2*digit if digit > d else 0
    aux //= 10
print(sum)