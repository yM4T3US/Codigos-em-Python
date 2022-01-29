tupla = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", 
"Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo", 
"Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", 
"Coritiba", "Avaí", "Ponte Preta", "Atlético Goianiense")
print("-=" * 30)
for i in range(5):
    print(tupla[i],end=" ")

print()
print("-=" * 30)

for k in range(-5, -1):
    print(tupla[k],end=" ")

print()
print("-=" * 30)

lista = []
for l in tupla:
    lista.append(l)
    lista.sort()

for j in lista:
        print(j,end=" | ")
print()
print("-=" * 30)

print(tupla.index("Chapecoense") + 1)
print("-=" * 30)
