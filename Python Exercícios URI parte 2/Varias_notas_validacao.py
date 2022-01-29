qtd = vit_gremio = vit_inter = emp = 0
while True:
    gols_inter, gols_gremio
    qtd += 1
    if inter > gremio:
        vit_inter += 1
    elif inter < gremio:
        vit_gremio += 1
    elif inter == gremio:
        emp += 1
    r = int(input("Novo grenal (1-sim 2-nao)"))
    if r == 2:
        break
print(f"{qtd} grenais\nInter:{vit_inter}\nGremio:{vit_gremio}\nEmpates:{emp}")
if vit_gremio == vit_inter:
    print("Nao houve vencedor")
elif vit_gremio > vit_inter:
    print("Gremio venceu mais")
elif vit_gremio < vit_inter:
    print("Inter venceu mais")
