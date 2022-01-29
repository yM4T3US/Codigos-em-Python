n = int(input())
for i in range(n):
    valores = input().split()
    if valores[0][-1 : (- (len(valores[1]))) - 1 : -1] != valores[1][-1::-1]:
        print("nao encaixa")
    else:
        print("encaixa")