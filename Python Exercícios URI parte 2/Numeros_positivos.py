A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())

qtd = 0
lista = [A, B, C, D, E]
for num in lista:
    if num % 2 == 0:
        qtd += 1
print('{} valores pares'.format(qtd))
