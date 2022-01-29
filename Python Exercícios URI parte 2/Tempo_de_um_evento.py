di = int(input().split()[1]) * 84600
lista = input().split(" : ")
hi, mi, si = int(lista[0]) * 3600, int(lista[1]) * 60, int(lista[2])
somai = hi + mi + si + di

df = int(input().split()[1]) * 84600
lista1 = input().split(" : ")
hf, mf, sf = int(lista1[0]) * 3600, int(lista1[1]) * 60, int(lista1[2])
somaf = hf + mf + sf + df

sub = somaf - somai

if sub < 0:
    sub += 84600

w = sub // 84600
r = sub % 84600 
x = r // 3600 + 1
r = r % 3600
y = r // 60 - 30
z = r % 60

print(f"{w} dia(s)\n{x} hora(s)\n{y} minuto(s)\n{z} segundo(s)")
 