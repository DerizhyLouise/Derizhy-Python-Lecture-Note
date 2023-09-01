def jumlahHuruf(a):
    a = a.upper()
    b = [0]*26
    for i in range(len(a)):
        c = ord(a[i])
        if(c>=65 and c<=90):
            b[c-65] += 1
    return b
    
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
    
    for i in range(len(b)):
        if(a[i]>0):
            print(b[i],a[i])

x = input()
x = jumlahHuruf(x)
sorting(x)