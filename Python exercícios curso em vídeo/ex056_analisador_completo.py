qtd_mulheres = 0
soma = 0
maior = 0
for c in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [masculino/feminino]: ')).upper()
    soma += idade
    if c == 1 and sexo == 'MASCULINO':
        maior = idade
        nome_maior = nome
    else:
        if sexo == 'MASCULINO':
            if idade > maior:
                maior = idade
                nome_maior = nome
    if sexo == 'FEMININO':
        if idade < 20:
            qtd_mulheres += 1
    print()

print(f'Média de idade do grupo = {soma / 4} '
      f'\nO homem mais velho é o {nome_maior}.'
      f'\nA quantidade de mulheres com idade inferior a 20 anos é {qtd_mulheres}')

