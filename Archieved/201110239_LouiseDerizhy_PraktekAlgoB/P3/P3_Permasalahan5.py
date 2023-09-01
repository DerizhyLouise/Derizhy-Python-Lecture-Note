print("Berikut adalah program untuk menghitung jarak hari dalam bahasa indonesia ke inggris")

hari = input("Masukkan nama hari: ")
jarak = int(input("Jarak hari ke depan: "))

if(hari == "senin"):
    x = 0
if(hari == "selasa"):
    x = 1
if(hari == "rabu"):
    x = 2
if(hari == "kamis"):
    x = 3
if(hari == "jumat"):
    x = 4
if(hari == "sabtu"):
    x = 5
if(hari == "minggu"):
    x = 6
else:
    print("Nama hari tidak terdefinisi")
    
hasil = jarak + x

if(hasil%7 == 0):
    y = 0
elif(hasil%7 == 1):
    y = 1
elif(hasil%7 == 2):
    y = 2
elif(hasil%7 == 3):
    y = 3
elif(hasil%7 == 4):
    y = 4
elif(hasil%7 == 5):
    y = 5
elif(hasil%7 == 6):
    y = 6
    
if(y == 0):
    print(hari,jarak,"monday")
if(y == 1):
    print(hari,jarak,"tuesday")
if(y == 2):
    print(hari,jarak,"wednesday")
if(y == 3):
    print(hari,jarak,"thursday")
if(y == 4):
    print(hari,jarak,"friday")
if(y == 5):
    print(hari,jarak,"saturday")
if(y == 6):
    print(hari,jarak,"sunday")