def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade >= 70:
        return "Facultativo"
    elif idade >= 18:
        return "Obrigatório"
    elif idade >= 16:
        return "Facultativo"
    elif idade < 16:
        return "Negado"


print(voto(int(input("Digite o ano de seu nascimento: "))))





