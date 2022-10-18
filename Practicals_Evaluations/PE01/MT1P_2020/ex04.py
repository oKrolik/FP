num = int(input("num? "))
count = 0
while num > 9:
    aux = 1
    while num != 0:
        aux = (num % 10) * aux
        num = num // 10
    num = aux
    count += 1
print(count)