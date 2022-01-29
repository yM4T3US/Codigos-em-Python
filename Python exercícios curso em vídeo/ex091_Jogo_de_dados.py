from random import randint
jogos = {}
temp = []
for i in range(1, 5):
    jogos["Jogador"] = input(f"Digite o nome do {i}º jogador: ")
    jogos["Resultado"] = randint(1, 6)
    temp.append(jogos.copy())

print(temp)

for k in range(len(temp)):
    if k == 0:
        maior = temp[k]["Resultado"]
        vencedor = temp[k]["Jogador"]
    else:
        if temp[k]["Resultado"] == maior:
            maior = temp[k]["Resultado"]
            vencedor = "Empate"
        if temp[k]["Resultado"] > maior:
            maior = temp[k]["Resultado"]
            vencedor = temp[k]["Jogador"]
if vencedor == "Empate":
    print("Houve empate.")
else:
    print(f"O vencedor foi {vencedor}")

