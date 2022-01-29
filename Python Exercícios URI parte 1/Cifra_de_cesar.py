n = int(input())
lista0 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", 
"O" ,"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lista1 = []
for i in range(n):
    lista = list(input())
    x = int(input())
    for k in lista:
        lista1.append(lista0[(lista0.index(k) - x)])
    for j in lista1:
        print(j, end="")
    print()
    lista1.clear()
