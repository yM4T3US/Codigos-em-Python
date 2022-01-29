from time import sleep
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
print()
while True:
    opcao = int(input("Escolha uma opção: "))
    print()
    if opcao == 1:
        print(f"Soma = {a + b}")
    elif opcao == 2:
        print(f"Multiplicação = {a * b}")
    elif opcao == 3:
        print(f"Maior = {max(a, b)}")
    elif opcao == 4:
        a = float(input("Digite um número: "))
        b = float(input("Digite outro número: "))
    elif opcao == 5:
        break
    print("=-=" * 10)
    sleep(2)

