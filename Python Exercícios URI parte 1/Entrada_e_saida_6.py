lista = input().split(".")
a = lista[1]
b = lista[0]
if (a[0]) == "0":
    if (a[1]) == "0":
        a = a[2:]
    else:
        a = a[1:]
c = a + "." + b
print(c)
