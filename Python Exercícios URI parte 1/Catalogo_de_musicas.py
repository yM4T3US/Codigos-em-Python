n = int(input())
lista = []
lista1 = []
lista2 = []
for i in range(n):
    x = input()
    lista.append([x])
    lista1.append(x.split("/"))

for k in lista1:
    for j in k:
        if ".mp3" in j:
            lista2.append(j)

for l in range(len(lista2)):
    if l == 0:
        minimo = lista2[l]
    else:
        if len(minimo) > len(lista2[l]):
            minimo = lista2[l]

for k in lista2:
    for j in k:
        if j == "Sampa.mp3":
            exclusao = k.index(j)
            palavras_antes = exclusao
            del k[:exclusao]
print(lista)
    



#lista1.append(len(x[-1 : x.index("/") : -1]))