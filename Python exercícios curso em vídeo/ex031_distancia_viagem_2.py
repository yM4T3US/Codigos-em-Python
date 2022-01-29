dist = float(input('Digite a distância da viagem em quilômetros: '))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'O preço da viagem é de {preco}')