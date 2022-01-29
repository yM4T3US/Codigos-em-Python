z = True
lista1 =[]
while z is True:
    lista = input().split()
    X = int(lista[0])
    Y = int(lista[1])
    if X != 0 and Y != 0:
        if X > 0 and Y > 0:
            lista1.append("primeiro")
        elif X > 0 and Y < 0:
            lista1.append("quarto")
        elif X < 0 and Y < 0:
            lista1.append("terceiro")
        elif X < 0 and Y > 0:
            lista1.append("segundo")
    else:
        z = False
for i in lista1:
    print(i)
