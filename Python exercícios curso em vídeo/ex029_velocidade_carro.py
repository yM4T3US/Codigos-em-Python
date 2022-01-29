vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7.00
    print('Você foi multado!' '\n' 'Valor da multa = R$ {:.2f}'.format(multa))
else:
    print('Você estava dentro do limite permitido de velocidade.')