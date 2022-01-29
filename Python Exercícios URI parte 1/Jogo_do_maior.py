while True:
    x = int(input())
    if x == 0:
        break
    a, b = 0, 0
    for i in range(x):
        lista = input().split()
        if int(lista[0]) > int(lista[1]):
            a += 1
        elif int(lista[0]) < int(lista[1]):
            b += 1
    print(f"{a} {b}")
  