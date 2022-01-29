N = int(input())

horas = N // 3600
r = N % 3600

minutos = r // 60
r = r % 60

segundos = r

print('{}:{}:{}'.format(horas, minutos, segundos))

