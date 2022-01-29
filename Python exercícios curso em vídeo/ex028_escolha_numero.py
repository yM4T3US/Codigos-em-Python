import random
lista = ['0', '1', '2', '3', '4', '5']
escolhido = random.choice(lista)
num = str(input('Escolha um número de 0 a 5: '))
if num == escolhido:
    print('Parabéns! Você acertou.')
else:
    print(f'Errou! O número escolhido foi {escolhido}')

