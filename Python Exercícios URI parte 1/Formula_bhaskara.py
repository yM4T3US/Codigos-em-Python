val = str(input()).split()
A = float(val[0])
B = float(val[1])
C = float(val[2])
d = (B ** 2) - 4 * A * C
if A != 0 and d >= 0:
    R1 = (-B + d ** (1 / 2)) / (2 * A)
    R2 = (-B - d ** (1 / 2)) / (2 * A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
else:
    print('Impossivel calcular')
