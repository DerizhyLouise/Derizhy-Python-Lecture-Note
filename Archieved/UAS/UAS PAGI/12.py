def hitungHuruf(a):
    x = a.upper()
    z = [0]*26
    for i in range(len(x)):
        y = ord(x[i])
        if(y>=65 and y<=90):
            z[y-65] += 1
    return z

def sorting(a):
    index = 65
    b = []
    while index <= 90:
        b.append(chr(index))
        index += 1

    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if(a[j]<=a[i]):
                temp1 = a[i]
                temp2 = b[i]
                a[i] = a[j]
                b[i] = b[j]
                a[j] = temp1
                b[j] = temp2
    
    for i in range(len(b)-1,-1,-1):
        if(a[i]>0):
            print(b[i],a[i])
            
x = input()
x = hitungHuruf(x)
sorting(x)