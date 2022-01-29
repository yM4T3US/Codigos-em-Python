X = int(input())
Y = int(input())
if X > Y:
    maior = X
    menor = Y
else:
    maior = Y
    menor = X
soma = 0
menor = menor + 1
while (menor < maior):
    if menor % 2 != 0:
        soma += menor
    menor += 1
print(soma)
