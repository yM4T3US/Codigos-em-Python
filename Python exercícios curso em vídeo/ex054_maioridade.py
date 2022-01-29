from datetime import date
menor = 0
maior = 0
ordem = 1
for ordem in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {ordem}ª pessoa: '))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Maiores de idade = {maior} '
      f'\nMenores de idade = {menor}')
