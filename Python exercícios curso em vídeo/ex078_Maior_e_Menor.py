lista = []
for i in range(1, 6):
    lista.append(int(input(f"Digite o {i} º valor: ")))
print(f"O maior valor da lista foi {max(lista)} e o menor foi {min(lista)}")
