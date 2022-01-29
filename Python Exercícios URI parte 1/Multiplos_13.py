X = int(input())
Y = int(input())
soma = 0
if X > Y:
    Z = Y
    Y = X
    X = Z
for num in range(X, Y + 1):
    if num % 13 != 0:
        soma += num
print(soma)
    
