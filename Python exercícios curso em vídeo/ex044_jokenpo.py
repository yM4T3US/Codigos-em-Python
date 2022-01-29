from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[0] - pedra
[1] - papel
[2] - tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou {}'.format(itens[computador]))
print('Usuário jogou {}'.format(itens[jogador]))





