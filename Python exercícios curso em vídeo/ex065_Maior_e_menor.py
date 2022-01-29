laco = True
rep = soma = 0
while laco == True:
    num = int(input("Digite um número: "))
    rep += 1
    if rep == 1:
        maior = menor = num
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    r = input("Deseja continuar [S/N]? ").upper().strip[0]
    if r == "N":
        laco = False
print(f"A média dos {rep} valores é {soma / rep}\nO maior valor digitado foi {maior} e o menor foi {menor}")


