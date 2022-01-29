n = int(input())
lista1 = []
for i in range(0, n):
    lista = input().split()
    a = int(lista[0])
    b = int(lista[1])
    c = b
    b = max(a, b)
    a = min(a, c)
    soma = 0
    for k in range(a + 1, b):
        if k % 2 != 0:
            soma += k
    lista1.append(soma)
for k in lista1:
    print (k)
