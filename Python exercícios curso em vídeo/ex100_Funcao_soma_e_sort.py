import random
lista = []
def sorteia(): 
    for i in range(5):
        lista.append(random.randint(0, 10))
def somaPar():
    soma = 0
    for k in lista:
        if k % 2 == 0:
            soma += k
    print(lista)
    print(soma)


sorteia()
somaPar()
    


