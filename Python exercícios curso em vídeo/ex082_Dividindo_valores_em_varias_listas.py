lista_completa = []
impares = []
pares = []
while True:
    valor = int(input())
    if valor < 0:
        break
    else:
        lista_completa.append(valor)
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
print("-="*30)
print("LISTA COMPLETA")
for i in lista_completa:
    if i == lista_completa[-1]:
        print(i)
    else:
        print(i, end=" -> ")
print("-="*30)
print("ÍMPARES")
for j in impares:
    if j == impares[-1]:
        print(j)
    else:
        print(j, end=" -> ")
print("-="*30)
print("PARES")
for k in pares:
    if k == pares[-1]:
        print(k)
    else:
        print(k, end= " -> ")
