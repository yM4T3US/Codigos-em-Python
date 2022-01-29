n = int(input())
for i in range(n):
    lista = ""
    mensagem = input()
    for k in mensagem:
        if k.islower():
            lista += k
    print(lista[-1::-1])
        