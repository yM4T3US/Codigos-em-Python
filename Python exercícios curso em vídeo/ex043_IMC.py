massa = float(input('Digite seu peso corporal: '))
altura = float(input('Digite sua altura: '))

imc = massa / altura ** 2

if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade mórbida.')

print('{}'.format(imc))
