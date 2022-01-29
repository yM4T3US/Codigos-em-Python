maior = 0
menor = 0
for ordem in range(1, 6):
    peso = float(input(f'Digite o peso da {ordem}ª pessoa: '))
    if ordem == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Maior peso = {maior}')
print(f'Menor peso = {menor}')
