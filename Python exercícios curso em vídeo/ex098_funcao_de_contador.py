def contador(inicio, fim, passo):
    if passo < 0:
        fim -= 1
    elif passo > 0:
        fim += 1
    for i in range(inicio, fim, passo):
        print(i, end=" ")


contador(int(input("Digite o início do intervalo: ")), int(input("Digite o fim: ")), int(input("Digite o passo do intervalo: ")))
