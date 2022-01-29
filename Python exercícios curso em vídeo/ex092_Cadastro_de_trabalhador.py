import datetime
cad = dict()
cad["Nome"] = input("Digite seu nome: ")
cad["Nasc."] = int(input("Digite o ano de seu nascimento: "))
cad["Idade"] = (datetime.datetime.now().year) - cad["Nasc."]
cad["CTPS"] = int(input("CTPS: "))
if cad["CTPS"] != 0:
    contr = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite o valor do seu salário: "))
    ano_apos = contr + 35
    cad["Aposentadoria"] = ano_apos - cad["Nasc."]
print(cad)