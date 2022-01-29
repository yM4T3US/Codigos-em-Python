def maior(* num):
    cont = 1
    while True:
        valor = int(input("Digite um valor: "))
        if cont == 1:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        if valor < 0:
            break
        cont += 1
    print(maior)

maior()

