A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())
qtd = 0
soma = 0
lista = [A, B, C, D, E, F]
for c in lista:
    if c > 0:
        qtd += 1
        soma += c
media = soma / qtd
print('{} valores positivos''\n''{:.1f}'.format(qtd, media))
