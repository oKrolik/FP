n_base = input()
base = 4
n_convertido = 0
for i in range(len(n_base)):
    n_convertido = n_convertido * base + int(n_base[i])
print(n_convertido)
