def ubahInt(a):
    b = []
    for i in range(len(a)):
        b.append(int(a[i]))
    return b

def sorting(a,b):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if(a[j]<=a[i]):
                temp1 = a[i]
                a[i] = a[j]
                a[j] = temp1
    
    for i in range(len(b)-1):
        for j in range(i+1, len(b)):
            if(b[j]>=b[i]):
                temp2 = b[i]
                b[i] = b[j]
                b[j] = temp2
    
    for i in range(5):
        print(a[i],b[i])
        
x = []
y = []
for i in range (5):
    x1, y1 = input().split()
    x.append(x1)
    y.append(y1)

x = ubahInt(x)
y = ubahInt(y)
sorting(x,y)