def fatorial(a, show=False):  
    fat = 1
    for i in range(a, 0, -1):
        if show == True:
            print(i, end="")
            if i > 1:
                print(" X ", end="")
            else:
                print(f" = ", end="")
        fat *= i
    return fat

print(fatorial(5, show=True))       

