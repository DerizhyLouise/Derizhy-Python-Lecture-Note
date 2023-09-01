banyak = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

jumlah = 0
m = 0
n = 0

for i in range(len(x)):
    jumlah += x[i]
    m += 1
    
    if m == banyak:
        if jumlah > y[n]:
            print(">")
        elif jumlah < y[n]:
            print("<")
        else:
            print("=")
        
        jumlah = 0
        m = 0
        n += 1