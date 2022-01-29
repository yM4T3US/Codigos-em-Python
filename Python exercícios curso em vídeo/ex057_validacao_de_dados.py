sexo = str(input("Digite seu sexo [M - F] ")).strip()
primeira_letra = sexo[0].upper()
while primeira_letra not in "MF":
    primeira_letra = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")