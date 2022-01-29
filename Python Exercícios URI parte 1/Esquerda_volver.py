lista = ["N", "L", "S", "O"]
while True:
    x = int(input())
    if x == 0:
        break
    lista1 = list(input())
    if x == 0:
        break
    direcao = 0
    for posicao in lista1:
        if posicao == "E":
            direcao -= 1
        elif posicao == "D":
            direcao += 1
        if direcao == -4 or direcao == 4:
            direcao = 0
    print(lista[direcao])
