n = int(input())
for i in range(n):
    k = int(input())
    idiomas = []
    for j in range(k):
        idiomas.append(input())
    lan = idiomas[0]
    for p in idiomas:
        if p != lan:
            lan = "ingles"
            break
    print(lan)


    
    

        

        

            
            

        


    