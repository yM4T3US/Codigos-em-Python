while True:
    try:
        valores = input().split()
        a = int(valores[0])
        b = int(valores[1])
        fatA = 1
        fatB = 1
        for i in range(1, a + 1):
            fatA = fatA * i
        for j in range(1, b + 1):
            fatB = fatB * j
        soma = fatA + fatB
        print(soma)
      
    except:
        break



