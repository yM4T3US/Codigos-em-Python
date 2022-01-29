n = int(input())
lista1 = []
for j in range(n):
    lista = input()
    soma = 0
    for i in lista:
        j = int(i)
        if j == 0 or j == 6 or j == 9:
            soma += 6
        elif j == 1:
            soma += 2
        elif j == 2 or j == 3 or j == 5:
            soma += 5
        elif j == 4:
            soma += 4
        elif j == 7:
            soma += 3
        elif j == 8:
            soma += 7
    lista1.append(soma)
for k in lista1:
    print(f"{k} leds")   
        