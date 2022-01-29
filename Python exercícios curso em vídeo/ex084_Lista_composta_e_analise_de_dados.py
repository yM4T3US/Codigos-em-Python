dados = []
dados1 = []
r = "S"
maior = menor = 0
while r in "Ss":
    nome = input("Nome: ")
    massa = float(input("Peso: "))
    dados1.append(nome)
    dados1.append(massa)
    if len(dados) == 0:
        maior = menor = dados1[1]
    else:
        if dados1[1] > maior:
            maior = dados1[1]
        if dados1[1] < menor:
            menor = dados1[1]
    dados.append(dados1[:])
    dados1.clear()
    print("Deseja continuar? [S/N]")
    r = input().upper()
print("-="*30)
for k in dados:
    print(f"""Nome: {k[0]}
Massa corporal: {k[1]}""")
    print("-="*30)
print()
print(f"Você cadastrou {len(dados)} pessoas.")
print()
for p in dados:
    if p[1] == maior:
        print(f"Maior(es) peso(s): {p[0]}")


        
