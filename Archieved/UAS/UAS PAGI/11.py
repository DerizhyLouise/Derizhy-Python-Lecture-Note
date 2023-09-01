def jumlah(x):
    z = [0]*127
    for i in range(len(x)):
        y = ord(x[i])
        if y > 0 and y <= 127:
            z[y] += 1
    
    index = 0
    for i in range(len(z)):
        if z[i] > 0:
            print(chr(i),"=",z[i])
            index += 1

def jenis(x):
    x = list(dict.fromkeys(x))
    for i in range(len(x)):
        if ord(x[i]) >= 97 and ord(x[i]) <= 122:
            print(x[i],"= Huruf Kecil")    
        elif ord(x[i]) >= 65 and ord(x[i]) <= 90:
            print(x[i],"= Huruf Besar")
        elif ord(x[i]) >= 48 and ord(x[i]) <= 57:
            print(x[i],"= Angka")
        else:
            print(x[i],"= Simbol")
            
def ascii(x):
    x = list(dict.fromkeys(x))
    y = []
    for i in range(len(x)):
        z = ord(x[i])
        if z > 0 and z <= 127:
            y.append(z)
    
    for i in range(len(y)):
        print(x[i],"=",y[i])

x = input()
print("----------------------------------------")
print("Jenis Karakter")
jenis(x)
print("----------------------------------------")
print("Kode ASCII Karakter")
ascii(x)
print("----------------------------------------")
print("Jumlah Karakter")
jumlah(x)
