lista = []
for i in range(1, 6):
    entrada = int(input(f"Digite o {i} º valor: "))
    if i == 1 or i > lista[-1]:
        lista.append(entrada)
    else:
        pos = 0
        while pos < len(lista):
            if entrada <= lista[pos]:
                lista.insert(pos, entrada)
                break
            pos += 1
print("-=" * 30)
print(f"Os valores digitados em ordem foram {lista}")

        
        


