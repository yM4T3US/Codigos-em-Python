from datetime import date

nasc = int(input('Digite sua data de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
