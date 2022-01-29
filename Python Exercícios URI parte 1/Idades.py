i, soma, cont = True, 0, 0

while i:
    age = int(input())
    if age < 0:
        i = False
    else:
        cont += 1
        soma += age
print(f"{(soma / cont):.2f}")
