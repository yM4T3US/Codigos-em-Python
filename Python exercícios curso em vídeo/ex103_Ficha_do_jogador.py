def ficha(jog= "desconhecido", gol=0):
    print(f"O jogador {jog} marcou {gol} gols no campeontato.")


n = str(input("Digite o nome do jogador: "))
g = str(input("Digite a quantidade de gols marcada pelo jogador: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)





