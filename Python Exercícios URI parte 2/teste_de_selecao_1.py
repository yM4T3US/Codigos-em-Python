lista = input().split()
A = int(lista[0])
B = int(lista[1])
C = int(lista[2])
D = int(lista[3])
somaCD = C + D
somaAB = A + B
if (B > C) and (D > A) and (somaCD > somaAB) and (C > 0) and (D > 0) and (A % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
