'''num = int(input('Digite um número: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        div += 1
if div == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível por {} vezes'.format(num, tot))
if tot == 2:
    print(f'Logo, {num} é primo.')
else:
    print(f'Logo, {num} não é primo.')

