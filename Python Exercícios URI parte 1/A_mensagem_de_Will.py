while True:
    try:
        mensagem = input()
        num_lampadas = int(input())
        lista2 = ""
        lista = [int(i) for i in input().split()]
        for i in lista:
            lista2 += mensagem[i - 1]
        print(lista2)        
    except EOFError:
        break
