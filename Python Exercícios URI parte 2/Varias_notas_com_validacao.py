r = 1
while r == 1:
    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print("nota invalida")
        n1 = float(input())
    n2 = float(input())   
    while n2 < 0 or n2 > 10:
        print("nota invalida")
        n2 = float(input())
    media = (n1 + n2) / 2
    print(f"media = {media:.2f}")
    r = True
    while r is True:
        print("novo calculo (1-sim 2-nao)")
        r = int(input())
        if r == 1:
            break
        elif r == 2:
            break
        elif r != 2 and r != 1:
            r = True
