valor = int(input())

n100 = valor // 100
r = valor % 100

n50 = r // 50
r = r % 50

n20 = r // 20
r = r % 20

n10 = r // 10
r = r % 10

n5 = r // 5
r = r % 5

n2 = r // 2
n1 = r % 2

print(valor)
print(n100, 'nota(s) de R$ 100,00')
print(n50, 'nota(s) de R$ 50,00')
print(n20, 'nota(s) de R$ 20,00')
print(n10, 'nota(s) de R$ 10,00')
print(n5, 'nota(s) de R$ 5,00')
print(n2, 'nota(s) de R$ 2,00')
print(n1, 'nota(s) de R$ 1,00')
