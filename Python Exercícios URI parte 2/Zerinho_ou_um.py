while True:
    try:
        lista = input().split()
        a, b, c = int(lista[0]), int(lista[1]), int(lista[2])
        if a == b and b == c:
            print("*")
        elif a == b and b != c:
            print("C")
        elif a == c and c != b:
            print("B")
        elif c == b and b != a:
            print("A")
    except:
        break
