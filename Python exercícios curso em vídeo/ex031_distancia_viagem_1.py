dist = float(input('Digite a distância da viagem em quilômetros: '))
if dist <= 200:
    valor = 0.5 * dist
else:
    valor = 0.45 * dist
print(f'O valor da viagem é de R$ {valor:.2f}')