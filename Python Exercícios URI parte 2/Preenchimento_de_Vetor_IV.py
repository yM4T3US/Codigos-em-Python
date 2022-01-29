par, impar = [], []

for i in range(15):

    x = int(input())

    # verifica se é par ou ímpar 
    if(x % 2 == 0):
        par.append(x)
    else:
        impar.append(x)

    
    # verifica se o tamanho da lista é 5     
    if(len(par) == 5):
        indice = 0

        #imprime a lista
        for v in par:
            print("par[{}] = {}" .format(indice,v))
            indice += 1
        
        # lista par recebe lista vazia
        par = []

    # mesmas instruções par
    if(len(impar)==5):
        indice = 0
        for v in impar:
            print("impar[{}] = {}" .format(indice,v))
            indice += 1
        impar = []


# depois de limpar as listas, elas vão ficar menores que 5 aí vai cair aqui
if(len(impar) > 0):
    indice = 0
    for v in impar:
        print("impar[{}] = {}" .format(indice,v))
        indice += 1

if(len(par)>0):
    indice = 0
    for v in par:
        print("par[{}] = {}" .format(indice,v))
        indice += 1
