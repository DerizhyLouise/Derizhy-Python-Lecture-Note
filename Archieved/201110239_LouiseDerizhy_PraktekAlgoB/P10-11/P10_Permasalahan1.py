def sorting(x):
    for i in range (len(x)-1):
        for j in range(i+1, len(x)):
            if(x[j]<=x[i]):
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x

def kecil(x,y):
    hasil = 0
    for i in range(y):
        hasil += x[i]
    return hasil
    
def besar(x,y):
    hasil = 0
    i = len(x) - 1
    j = len(x) - y
    while i >= j:
        hasil += x[i]
        i -= 1
    return hasil

x = [int(i) for i in input().split()]
y = int(input())
x = sorting(x)

print(kecil(x,y),besar(x,y))