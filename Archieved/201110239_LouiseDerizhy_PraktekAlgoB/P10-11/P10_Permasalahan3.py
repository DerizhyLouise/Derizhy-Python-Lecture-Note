def cek (x,y):
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if(x[j]<x[i]):
                temp1 = x[i]
                temp2 = y[i]
                x[i] = x[j]
                y[i] = y[j]
                x[j] = temp1
                y[j] = temp2
    return y

x = input().split()
y = input()
b = []

for i in range(len(x)):
    a = x[i]
    b.append(len(a))
    
c = cek(b,x)
if(y=="asc"):
    for i in range(len(c)):
        print(c[i])
elif(y=="desc"):
    for i in range(len(c)-1, -1, -1):
        print(c[i])