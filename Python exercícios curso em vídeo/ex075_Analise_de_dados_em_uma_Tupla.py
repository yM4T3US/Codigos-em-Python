tupla = (int(input()), int(input()), int(input()), int(input()), int(input()))
nove = 0
for i in tupla:
    if i == 9:
        nove += 1
    elif i == 3:
        print(f"{tupla.index(3)} -> posição do primeiro 3")
for k in tupla:
    if k % 2 == 0:
        print(f"{i} -> par")
print(f"{nove} -> quantidade de noves")
