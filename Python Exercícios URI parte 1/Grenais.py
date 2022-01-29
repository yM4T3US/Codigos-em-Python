resposta = 1
vit_gremio = 0
vit_inter = 0
empates = 0
grenais = 0
while resposta == 1:
    lista = input().split()
    gols_inter = int(lista[0])
    gols_gremio = int(lista[1])
    if gols_gremio > gols_inter:
        vit_gremio += 1
    elif gols_gremio < gols_inter:
        vit_inter += 1
    elif gols_gremio == gols_inter:
        empates += 1
    grenais += 1
    resposta = int(input("Novo grenal (1-sim 2-nao)"))


print(f"{grenais} grenais\nInter:{vit_inter}\nGremio:{vit_gremio}\nEmpates:{empates}")

if vit_inter > vit_gremio:
    print("Inter venceu mais")
elif vit_inter < vit_gremio:
    print("Gremio venceu mais")
elif vit_inter == vit_gremio:
    print("Nao houve vencedor")
    