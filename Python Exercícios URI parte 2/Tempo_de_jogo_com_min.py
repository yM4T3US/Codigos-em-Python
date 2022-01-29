lista = input().split()

hora_inicial = int(lista[0])
min_inicial = int(lista[1])
hora_final = int(lista[2])
min_final = int(lista[3])

hora_inicial = hora_inicial * 60
tempo_total_1 = hora_inicial + min_inicial
hora_final = hora_final * 60
tempo_total_2 = hora_final + min_final

duracao = tempo_total_2 - tempo_total_1

if hora_inicial == hora_final:
    if min_inicial == min_final:
        duracao = 1440
    else:
        tempo_total3 = min_final - min_inicial
        duracao = tempo_total3 + 1440

if duracao < 0:
    duracao += 1440


h = duracao // 60
minuto = duracao % 60

if h >= 24 and minuto > 0:
    h -= 24


print(f"O JOGO DUROU {h} HORA(S) E {minuto} MINUTO(S)")





