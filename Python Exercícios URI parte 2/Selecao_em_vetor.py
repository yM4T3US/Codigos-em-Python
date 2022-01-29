a = []
for i in range(100):
    valor = float(input())
    a.append(valor)
    if valor <= 10:
        print(f"A[{i}] = {valor:.1f}")
