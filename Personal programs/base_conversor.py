n_decimal = int(input("Decimal para a base que preferir: "))
base = int(input("BASE: "))
n_convertido = potencia = 0
while n_decimal:
    n_convertido = n_decimal % base * 10 ** potencia + n_convertido
    n_decimal //= base
    potencia += 1
print(str(n_convertido))


n_base = input("Numero a ser convertido para decimal: ")
base = int(input("BASE: "))
n_convertido = 0
for i in range(len(n_base)):
    n_convertido = n_convertido * base + int(n_base[i])
print(n_convertido)
