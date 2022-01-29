dicionario = dict()
dicionario["Nome"] = str(input("Nome: "))
dicionario["Media"] = float(input("Média: "))
if dicionario["Media"] >= 7:
    dicionario["Situação"] = "Aprovado"
elif 5 <= dicionario["Media"] < 7:
    dicionario["Situação"] = "Recuperação"
else:
    dicionario["Situação"] = "Reprovado"
print("-="*15)
for k, v in dicionario.items():
    print(f"{k} é igual a {v}")
print("-="*15)    