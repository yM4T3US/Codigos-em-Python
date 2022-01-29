n = int(input())
a, b, cont = -1, 1, 0
while cont < n:
    c = a + b
    if cont == n - 1:
        print(c)
    else:
        print(c, end=" ")
    a = b
    b = c
    cont += 1
