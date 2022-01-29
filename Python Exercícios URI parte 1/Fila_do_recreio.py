n = int(input())
for i in range(n):
    alunos = int(input())
    lista = input().split()
    lista1 = list(map(int, lista))
    lista2 = sorted(lista1, reverse=True)
    soma = 0
    for k in range(0, alunos):
        if lista2[k] == lista1[k]:
            soma += 1      
    print(soma)
