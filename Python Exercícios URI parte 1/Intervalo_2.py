A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
lista = [A, B, C, D, E]
par = 0
imp = 0
pos = 0
neg = 0
for c in lista:
    if c % 2 == 0:
        par += 1
    else:
        imp += 1
    if c > 0:
        pos += 1
    elif c < 0:
        neg += 1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
