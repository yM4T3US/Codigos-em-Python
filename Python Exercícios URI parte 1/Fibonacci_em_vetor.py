lista = [0, 1]
lista1 = []
t = int(input())
for i in range(t):
    x = int(input())
    lista1.append(x)
l = max(lista1)
a = 0
b = 1
for i in range(l):
    soma = a + b
    lista.append(soma)
    c = b
    b = soma
    a = c
for k in lista1:
    print(f"Fib({k}) = {lista[k]}")

