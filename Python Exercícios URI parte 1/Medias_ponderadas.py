import time
I = time.time()
N = int(input())
list1 = []
for i in range(N):
    lista = input().split()
    MA = (float(lista[0]) * 2 + float(lista[1]) * 3 + float(lista[2]) * 5) / 10
    list1.append(f'{MA:.1f}')
for c in list1:
    print(c)
F = time.time()
print(F - I)






