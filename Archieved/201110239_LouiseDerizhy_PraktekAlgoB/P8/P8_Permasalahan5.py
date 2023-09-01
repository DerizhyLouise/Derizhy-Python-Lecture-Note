def jamPasir(x):
    s1 = "*"
    s2 = "."
    i = x
    j = 1
    
    while i >= 1:
        if(i==x):
            jumlah = 1 + (i-1)*2
            print(s1*jumlah)
        elif(i<=x and i>1):
            jumlah = 1 + (i-2)*2
            print(" "*j,s1,s2*jumlah,s1,sep="")
            j+=1
        elif(i==1):
            j-=1
            print(" "*j,s2)
        i-=1
    
    k = 1
    
    while k <= x-1:
        if(k>=1 and k<x-1):
            jumlah = 1 + (k-1)*2
            print(" "*j,s1,s2*jumlah,s1,sep="")
            j-=1
        elif(k==x-1):
            jumlah = 1 + (k)*2
            print(s1*jumlah)
        k+=1

n = int(input())
jamPasir(n)