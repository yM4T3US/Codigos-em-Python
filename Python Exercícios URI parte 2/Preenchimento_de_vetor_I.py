n = []
x = int(input())
for i in range(10):
    n.append(x)
    x = 2 * x
for k in range(10):
    print(f"N[{k}] = {n[k]}")
