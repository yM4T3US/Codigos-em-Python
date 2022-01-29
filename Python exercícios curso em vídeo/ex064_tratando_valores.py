cont = soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f"{cont} números foram digitados e a soma desses números é {soma}.")
