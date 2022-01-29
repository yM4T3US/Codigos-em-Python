lista = []
print("Digite o número de valores que deseja inserir:")
n = int(input())
for i in range(1, n + 1):
    entrada = int(input(f"Digite o {i} º valor: "))
    if entrada not in lista:
        lista.append(entrada)
lista.sort()
for j in range(len(lista)):
    if j == len(lista) - 1:
        print(lista[j])
    else:
        print(lista[j], end=" -> ")
    
