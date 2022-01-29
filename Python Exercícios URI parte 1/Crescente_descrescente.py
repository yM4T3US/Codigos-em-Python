while True:
    lista = input().split()
    X = int(lista[0])
    Y = int(lista[1])
    if X > Y:
        print("Decrescente")
    elif X < Y:
        print("Crescente")
    elif X == Y:
        break
