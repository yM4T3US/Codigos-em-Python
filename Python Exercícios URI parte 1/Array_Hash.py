lista = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
testes = int(input())
lista1 = []
for j in range(testes):
    testes1 = int(input())
    soma = 0
    for i in range(testes1):
        lista1 = str(input().upper())
        cont = 0
        for k in lista1:
            soma += lista.index(k) + i + cont
            cont += 1
    print(soma)
        
