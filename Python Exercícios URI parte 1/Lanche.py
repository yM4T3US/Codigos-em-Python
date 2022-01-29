lista = input().split()

a = int(lista[0])
b = int(lista[1])

if a == 1:
    preco = 4.00 * b
elif a == 2:
    preco = 4.50 * b
elif a == 3:
    preco = 5.00 * b
elif a == 4:
    preco = 2.00 * b
elif a == 5:
    preco = 1.50 * b

print('Total: R$ {:.2f}'.format(preco))
