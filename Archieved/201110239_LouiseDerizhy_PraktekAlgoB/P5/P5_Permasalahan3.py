print("Program Pembilang per Penyebut")

x = int(input())
y = int(input())
a = int(input())
b = int(input())
loop = int(input())

hasil = x//y
if(hasil == 0):
    print(x,"/",y,sep="")
else:
    print(hasil)

for i in range(loop-1):
    if(hasil == 1):
        hasil = x//y
        x += a
        y += b
        print(hasil)
    else:
        x += a
        y += b    
        print(x,"/",y,sep="")