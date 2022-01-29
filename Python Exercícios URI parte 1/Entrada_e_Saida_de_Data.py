lista = input().split("/")
mes = lista[1]
dia = lista[0]
ano = lista[2]
print(f"{mes}/{dia}/{ano}")
print(f"{ano}/{mes}/{dia}")
print(f"{dia}-{mes}-{ano}")
