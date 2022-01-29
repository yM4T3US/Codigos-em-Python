x = int(input())
i = [int(l) for l in input().split()]
soma = 0
for k in i:
    if k == x:
        soma += 1
print(soma)
