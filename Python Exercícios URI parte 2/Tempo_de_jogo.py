lista = input().split()
h_inicial = int(lista[0])
h_final = int(lista[1])
if h_inicial >= h_final:
    tempo = 24 - h_inicial + h_final
else:
    tempo = h_final - h_inicial
print(f'O JOGO DUROU {tempo} HORA(S)')

