n = int(input())
for i in range(n):
    lista = input()
    one, two = 0, 0
    if len(lista) == 3:
        if lista[0] == "o":
            one += 1
        elif lista[0] == "t":
            two += 1
        if lista[1] == "n":
            one += 1
        elif lista[1] == "w":
            two += 1
        if lista[2] == "e":
            one += 1
        elif lista[2] == "o":
            two += 1
        if one > two:
            print("1")
        elif one < two:
            print("2")
    else:
        print("3")
        
        