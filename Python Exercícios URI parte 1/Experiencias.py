N = int(input(""))
coelhos = 0
ratos = 0
sapos = 0
total = 0
for i in range(N):
    lista = str(input()).split()
    if lista[1] == "C":
        coelhos += int(lista[0])
    elif lista[1] == "R":
        ratos += int(lista[0])
    elif lista[1] == "S":
        sapos += int(lista[0])
    total += int(lista[0])
print(f"Total: {total} cobaias\nTotal de coelhos: {coelhos}\nTotal de ratos: {ratos}\nTotal de sapos: {sapos}")
print(f"Percentual de coelhos: {100 * coelhos / total:.2f} %\nPercentual de ratos: {100 * ratos / total:.2f} %\nPercentual de sapos: {100 * sapos / total:.2f} %")
