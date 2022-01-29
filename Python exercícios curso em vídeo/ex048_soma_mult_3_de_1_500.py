soma = 0
cont = 0
for c in range(3, 499, 3):
    if c % 2 != 0:
        soma += c
        cont += 1
print(soma)
print(cont)