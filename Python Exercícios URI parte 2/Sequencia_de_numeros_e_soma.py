lista[1] = []
rep = 1
while a <= 0 or b <= 0:
    lista = input().split()
    a = int(lista[0])
    b = int(lista[1])
    if a > b:
        d = a
        a = b
        b = a
    for i in range(a, b + 1):
        lista[rep].append(i)
        soma += i
    lista[rep].append(soma)
    rep += 1

