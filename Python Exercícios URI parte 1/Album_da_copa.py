n = int(input())
b = int(input())
lista = []
for i in range(1, n + 1):
    lista.append(i)
for k in range(1, b + 1):
    a = int(input())
    if a in lista:
        lista.remove(a)
print(len(lista))
