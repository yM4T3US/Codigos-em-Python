from random import randint
print("-="*15)
print(f"{'MEGA SENA':^30}")
print("-="*15)
print()

n = int(input("Quantos jogos serão gerados? "))

print()
print("="*30)

lista = []
temp = []

for i in range(n):
    for k in range(6):
        temp.append(randint(1, 60))
    lista.append(temp[:])
    temp.clear()

for j in range(0, len(lista)):
    print(f"{j + 1}º jogo:")
    for z in range(6):
        if z == 5:
            print(f"{lista[j][z]}")
        else:
            print(f"{lista[j][z]}", end=" → ")
    print("="*30)


