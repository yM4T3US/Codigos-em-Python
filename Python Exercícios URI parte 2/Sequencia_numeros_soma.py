z = True
lista1 = []
while z is True:
    lista = input().split()
    M, N = int(lista[0]), int(lista[1])
    if M > 0 and N > 0:
        lista1.append(M, N)
    else:
        break
lista1.sort()
soma = 0
for i in lista1:
    soma += i
print(f"{lista} Sum={soma}")