N = int(input())
inn = 0
out = 0
for x in range(0, N):
    c = int(input())
    if 10 <= c <= 20:
        inn += 1
    else:
        out += 1
print('{} in''\n''{} out'.format(inn, out))
