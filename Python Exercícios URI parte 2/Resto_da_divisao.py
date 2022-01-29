X = int(input())
Y = int(input())
lista = []
if X > Y:
    Z = X
    X = Y
    Y = Z

for i in range(X + 1, Y):
    if i % 5 == 2 or i % 5 == 3:
        lista.append(i)

for c in lista:
    print(c)

