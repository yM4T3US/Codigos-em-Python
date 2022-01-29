idade = int(input())

ano = idade // 365
r = idade % 365

mes = r // 30
r = r % 30

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(r))
