x = []
for i in range(10):
    a = int(input())
    if a <= 0:
        x.append(1)
    else:
        x.append(a)
for i in range(10):
    print(f"X[{i}] = {x[i]}")
