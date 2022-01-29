sal = float(input())

if 0 <= sal <= 400.00:
    x = 0.15
elif sal <= 800.00:
    x = 0.12
elif sal <= 1200.00:
    x = 0.10
elif sal <= 2000.00:
    x = 0.07
else:
    x = 0.04

novosal = sal + x * sal
reajuste = x * sal
perc = x * 100

print('Novo salario: {:.2f}'.format(novosal))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'. format(int(perc)))