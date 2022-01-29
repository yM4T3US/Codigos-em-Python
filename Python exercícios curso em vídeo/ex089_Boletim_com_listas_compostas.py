l_completa = []
l_temp = []
while True:
    l_temp.append(input("Digite o nome do aluno: "))
    l_temp.append(float(input("Digite a primeira nota: ")))
    l_temp.append(float(input("Digite a segunda nota: ")))
    l_completa.append(l_temp[:])
    l_temp.clear()
    r = input("Deseja continuar [S/N] ").upper()
    if r[0] == "N":
        break
print("-="*15)
print(f"{'BOLETIM':^30}")
print("-="*15)
print(f"{'NOME':<10} {'MÉDIA':>8}")
print()
for i in l_completa:
    print(f"{i[0]:<10} {(((i[1] + i[2]) / 2)):>8.1f}")
    




