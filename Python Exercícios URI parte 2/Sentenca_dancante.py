while True:
    try:
        lista = input()
        lista1 = list(lista)
        lista2 = []
        l = 0
        for k in lista1:
            if k.isspace():
                lista2.append(" ")
            else:
                if l % 2 == 0:
                    lista2.append(k.upper())
                else:
                    lista2.append(k.lower())
                l += 1
        for k in lista2:
            print(k,end="")
        print()
    except:
        break
