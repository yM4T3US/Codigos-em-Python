lista = []
soma = 0
soma1 = 0
while soma != 2:
    n1 = float(input())
    if n1 >= 0 and n1 <= 10:
        soma += 1
        soma1 += n1
        if soma == 2:
            break
    else:
        lista.append(0)
    n2 = float(input())
    if n2 >= 0 and n2 <= 10:
        soma += 1
        soma1 += n2
    else:
        lista.append(0)
lista.append(f"{(soma1 / 2):.2f}")
for j in lista:
    if j == 0:
        print("nota invalida")
    else:
        print(f"media = {j}")

