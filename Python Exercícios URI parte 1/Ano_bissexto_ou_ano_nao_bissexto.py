d = False
while True:
    try:
        x = int(input())
        if d == True:
            print()
        a = False
        b = False
        c = False
        d = False
        if x % 4 == 0 or x % 400 == 0 and x % 100 != 0:
            print("This is leap year.")
            a = True
            if x % 55 == 0:
                b = True
        if x % 15 == 0:
            print("This is huluculu festival year.")
            c = True
        if b == True:
            print("This is bulukulu festival year.")
        if a == False and b == False and c == False:
            print("This is an ordinary year.")
            d = True
    except:
        break
