def perkalian(x,y,baris1,kolom2):
    a = kali(x,3)
    b = kali(y,2)
    c = baris1 * [0]
    
    for i in range(baris1):
        c[i] = kolom2 * [0]
        
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def kali(x,y):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = y*x[i][j]
    return x

def matriks(baris):
    m = baris*[0]
    for i in range(baris):
        arr = [int(i) for i in input().split()]
        m[i] = arr
    return m
        
baris1, kolom1 = input().split()
baris2, kolom2 = input().split()

baris1 = int(baris1)
baris2 = int(baris2)
kolom1 = int(kolom1)
kolom2 = int(kolom2)

m1 = matriks(baris1)
m2 = matriks(baris2)
c = perkalian(m1,m2,baris1,kolom2)

for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j],end=" ")
    print()