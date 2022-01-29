list = input().split()
A = int(list[0])
B = int(list[1])
if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
