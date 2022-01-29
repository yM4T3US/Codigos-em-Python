x = int(input())
j = 0
cont = 0
while cont < 1000:
    print(f"N[{cont}] = {j}")
    cont += 1
    if j == x - 1:
        j = 0
    else:
        j += 1