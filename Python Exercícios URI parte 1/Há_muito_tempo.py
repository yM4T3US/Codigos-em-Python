n = int(input())
atual = 2015
lista = []
for i in range(n):
    num = int(input())
    if num < atual:
        duracao = atual - num
        dur = str(duracao) + " D.C."
    elif num >= atual:
        duracao = (atual - num - 1) * - 1
        dur = str(duracao) + " A.C."
    lista.append(dur)
for k in lista:
    print(k)
