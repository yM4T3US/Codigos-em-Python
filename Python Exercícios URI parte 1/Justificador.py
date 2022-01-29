while True:
    n = int(input())
    if n == 0:
        break
    lista = []
    lista1 = []
    lista2 = []
    for i in range(n):
        lista.append(input())
    for k in lista:
        lista1.append(len(k))
    for j in lista:
        print(f"{j:>{max(lista1)}}")
    print()
    
    
    
    
