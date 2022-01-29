matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for j in range(3):
    for k in range(3):
        valor = int(input(f"Digite um valor para a posição [{j}, {k}]: "))
        matriz[j][k] = valor

soma_pares, soma_terceira = 0, 0
for l in range(3):
    for m in range(3):
        if matriz[l][m] % 2 == 0:
            soma_pares += matriz[l][m]


for n in matriz:
    soma_terceira += n[2]

for o in matriz[1]:
    for p in range(3):
        if p == 0:
            maior = matriz[1][p]
        else:
            if matriz[1][p] > maior:
                maior = matriz[1][p]
print("-="*30)
for q in range(3):
    for r in range(3):
        print(f"[{matriz[q][r]:^5}]",end="")
    print()

print("-="*30)    
print(f"Soma de todos os valores pares = {soma_pares}")
print(f"Soma dos valores da terceira coluna = {soma_terceira}")
print(f"Maior valor da segunda linha = {maior}")


    


