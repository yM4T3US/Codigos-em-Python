list = input().split()
A = float(list[0])
B = float(list[1])
C = float(list[2])
if A < B + C and B < A + C and C < A + B:
    per = A + B + C
    print('Perimetro = {:.1f}'.format(per))
else:
   area = ((A + B) * C) / 2
   print('Area = {:.1f}'.format(area))

