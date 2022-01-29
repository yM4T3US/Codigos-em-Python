# ler o salário do funcionário
# calcular o valor de aumento
# > 1250 o percentual de aumento é de 10%
# <= 1250 15%

sal = float(input('Digite o valor do salário: '))
if sal > 1250:
    aum = sal + 0.10 * sal
else:
    aum = sal + 0.15 * sal
print(f'O salário com aumento é de R$ {aum:.2f}')
