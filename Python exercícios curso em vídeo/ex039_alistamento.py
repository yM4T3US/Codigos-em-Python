from datetime import date
nasc = int(input('Digite sua data de nascimento: '))
ano = date.today().year
alist = ano - nasc
if alist == 18:
    print('Chegou tua hora.')
elif alist < 18:
    calc = 18 - alist
    print(f'Faltam {calc} anos.')
elif alist > 18:
    calc = alist - 18
    print(f'Tá atrasado {calc} ano(s). Já deixa 10 aí.')
