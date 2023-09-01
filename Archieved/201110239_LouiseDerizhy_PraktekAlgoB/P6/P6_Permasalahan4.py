print("Program Plus Minus Jumlah")

''' 
a = banyak keluaran
b = pertambahan
c = nilai awal
'''

a,b,c = list(map(int,input().split()))
print(c)
total = (c + b) * -1
hasil = 0 + c + total

for i in range(a-1):
    if(i%2==0):
        print(total)
        total = (total*-1) + b
        hasil += total
    else:
        print(total)
        total = (total + b)*-1
        hasil += total

hasil -= total
print(hasil)