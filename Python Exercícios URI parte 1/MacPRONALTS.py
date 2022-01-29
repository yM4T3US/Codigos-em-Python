dic = {
    "1001": 1.50,
    "1002": 2.50,
    "1003": 3.50,
    "1004": 4.50,
    "1005": 5.50,
}

x = int(input())
soma = 0
for i in range(x):
    h = input().split()
    b = int(h[1])
    soma += dic[h[0]] * b

print(f"{soma:.2f}")