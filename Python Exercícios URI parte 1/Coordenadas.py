lista = input().split()
x = float(lista[0])
y = float(lista[1])
if x == 0 == y:
    print('Origem')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
elif x > 0:
    if y > 0:
        print('Q1')
    elif y < 0:
        print('Q4')
elif x < 0:
    if y > 0:
        print('Q2')
    elif y < 0:
        print('Q3')
