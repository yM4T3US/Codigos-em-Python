lista = [int(i) for i in input().split()]
jogador1_ganha = False
jogador1_roubou = False
resultado = lista[1] + lista[2]
if resultado % 2 == 0:
    if lista[0] == 1:
        jogador1_ganha = True
    elif lista[0] == 0:
        jogador1_ganha = False


if lista[3] == 1:
    jogador1_roubou = True
elif lista[3] == 0:
    jogador1_roubou = False


if lista[4] == 1:
    roubo_acusado = True
elif lista[4] == 0:
    roubo_acusado = False

if jogador1_ganha:
    if jogador1_roubou:
        if roubo_acusado == False:
            print("Jogador 1 ganha!")
        elif roubo_acusado == True:
            print("Jogador 2 ganha!")
    elif jogador1_roubou == False:
        if roubo_acusado == False:
            print("Jogador 1 ganha!")
        elif roubo_acusado == True:
            print("Jogador 1 ganha")
if jogador1_ganha == False:
    if jogador1_roubou == False:
        if roubo_acusado == False:
            print("Jogador 2 ganha!")
        if roubo_acusado == True:
            print("Jogador 1 ganha!")
    if jogador1_roubou == True:
        if roubo_acusado == False:
            print("Jogador 1 ganha!")
        elif roubo_acusado == True:
            print("Jogador 2 ganha!")







    