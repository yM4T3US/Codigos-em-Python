n = int(input())
valores = []
for i in range(n):
    soma = 0
    cont = 0
    lista = input().split()
    x = int(lista[0])
    y = int(lista[1])
    while cont < y:
        if x % 2 != 0:
            soma += x
            cont += 1
        x += 1
    valores.append(soma)
for k in valores:
    print(k)

