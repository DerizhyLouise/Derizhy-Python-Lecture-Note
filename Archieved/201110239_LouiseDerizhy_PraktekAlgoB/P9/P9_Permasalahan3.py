def cek1(a,b):
    for i in range(len(b)):
        x = []
        y = []
        for j in range(len(a)):
            if(b[i]>a[j]):
                x.append(a[j])
            elif(b[i]<a[j]):
                y.append(a[j])
        if(x==[]):
            print("X",min(y))
        elif(y==[]):
            print(max(x),"X")
        else: 
            print(max(x),min(y))

x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
cek1(x,y)