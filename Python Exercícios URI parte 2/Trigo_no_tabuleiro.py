n = int(input())
for i in range(n):
    n = int(input())
    sn = 1 * (2 ** n - 1)
    massa = sn / 12
    print(f"{int(massa / 1000)} kg")
