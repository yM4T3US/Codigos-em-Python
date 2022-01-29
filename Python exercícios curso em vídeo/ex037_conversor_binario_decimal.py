num = int(input('Digite um número: '))
escolha = int(input('Escolha: 1 para converter o número em binário, 2 para octal e 3 para hexadecimal '))
if escolha == 1:
    print('{} em binário é {:b}'.format(num, num))
elif escolha == 2:
    print('{} em octal é igual a {:o}'.format(num, num))
elif escolha == 3:
    print('{} em hexadecimal é igual a {:X}'.format(num, num))

