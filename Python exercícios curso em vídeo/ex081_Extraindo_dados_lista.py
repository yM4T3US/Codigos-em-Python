lista = []
cont = 1
while True:
    num = input(f"Digite o {cont} º número: ").upper()
    if num == "STOP":
        break
    else:
        lista.append(int(num))
    cont += 1
print(f"O total de números digitados foi de {len(lista)}")
lista.sort(reverse=True)
for i in lista:
    if i == lista[-1]:
        print(i)
    else:
        print(i, end=" -> ")
if 5 in lista:
    print(True)
else:
    print(False)