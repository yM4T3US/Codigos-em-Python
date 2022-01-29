n = int(input())
lista1 = []
for i in range(n):
    lista = input().split()
    a = int(lista[0])
    b = int(lista[1])
    if b == 0:
        lista1.append("divisao impossivel")
    else:
        lista1.append(f"{(a / b):.1f}")
for c in lista1:
    print(c)

    
    
        