def cekPrima(wew):
    data = []
    jumlah = 0

    for i in range(len(wew)):
        if(wew[i]!=1):
            j = 2
            while (wew[i]<=10000000):
                if(wew[i]%j==0):
                    if(wew[i]==j):
                        data.append(j)
                        break
                    else:
                        break
                j += 1
                
    print("Bilangan Prima:")
    
    for k in range(len(data)):
        print(data[k],end=" ")
        
    for l in range(len(data)):
        jumlah += data[l]
    
    rerata = jumlah/len(data)
    
    print()
    print("Rerata =","%.3f"%rerata)

x = [int(i) for i in input().split()]
         
cekPrima(x)