A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())

lista = [A, B, C, D, E, F]
pos = 0
for c in lista:
    if c > 0:
        pos += 1
print('{} valores positivos'.format(pos))

