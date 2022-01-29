valor_casa = float(input('Valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
tempo = int(input('Em quantos anos você deseja quitar a divida: '))
meses = tempo * 12
parcelas = valor_casa / meses
porcentagem = 0.3 * salario

if parcelas > porcentagem:
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado.')

