km = float(input('Digite a quantidade de km rodados:'))
dias = int(input('Digite a quantidade de dias:'))
preco = 60 * dias + 0.15 * km
print('O preço do aluguel do carro é de R$ {:.2f}'.format(preco))
