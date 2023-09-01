def asci(x):
    y = []
    for i in range(len(x)):
        if x[i] >= 0 and x[i] <= 255:
            y.append(chr(x[i]))
    return y

def jenis(x):
    y = []
    for i in range(len(x)):
        if ord(x[i]) >= 97 and ord(x[i]) <= 122:
            y.append("Huruf Kecil")  
        elif ord(x[i]) >= 65 and ord(x[i]) <= 90:
            y.append("Huruf Besar")
        elif ord(x[i]) >= 48 and ord(x[i]) <= 57:
            y.append("Angka")
        else:
            y.append("Simbol")
    return y

def jumlah(x):
    y = [0]*4
    for i in range(len(x)):
        z = ord(x[i])
        if z >= 0 and z <= 255:
            if ord(x[i]) >= 97 and ord(x[i]) <= 122:
                y[0] += 1
            elif ord(x[i]) >= 65 and ord(x[i]) <= 90:
                y[1] += 1
            elif ord(x[i]) >= 48 and ord(x[i]) <= 57:
                y[2] += 1
            else:
                y[3] += 1
    return y

    
x = [int(i) for i in input("Kumpulan angka (0 s/d 255) : ").split()]
a = asci(x)
b = jenis(a)
c = jumlah(a)
arr = ["Huruf Kecil","Huruf Besar","Angka","Simbol"]

for i in range(len(x)):
    if x[i] < 10:
        print(" ",x[i],": ",a[i],"\tadalah",b[i])
    if x[i] >= 10 and x[i] < 100:
        print("",x[i],": ",a[i],"\tadalah",b[i])
    if x[i] >= 100:
        print(x[i],": ",a[i],"\tadalah",b[i])
print()
for i in range(len(arr)):
    if i < 2:
        print(arr[i],"\tBerjumlah : ",c[i],"|","*"*c[i])
    else:
        print(arr[i],"\t\tBerjumlah : ",c[i],"|","*"*c[i])