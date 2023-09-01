print("Berikut adalah program untuk mengukur validitas sebuah tanggal")

tanggal = int(input("Masukkan tanggal: "))
bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun: "))

y = "valid"
n = "tidak valid"

validTahun = False
kabisat = False
validBulan = False

if(tahun >= 1900 and tahun <= 2099):
    validTahun = True

if(tahun%4 == 0):
    kabisat = True
    
if(bulan > 0 and bulan <= 12):
    validBulan = True

if(bulan == 1):
    maxTanggal = 31
    namaBulan = "januari"
elif(bulan == 2):
    if(kabisat):
        maxTanggal = 29
        namaBulan = "februari"
    else:
        maxTanggal = 28
        namaBulan = "februari"
elif(bulan == 3):
    namaBulan = "maret"
    maxTanggal = 31
elif(bulan == 4):
    maxTanggal = 30
    namaBulan = "april"
elif(bulan == 5):
    maxTanggal = 31
    namaBulan = "may"
elif(bulan == 6):
    maxTanggal = 30
    namaBulan = "juni"
elif(bulan == 7):
    maxTanggal = 31
    namaBulan = "juli"
elif(bulan == 8):
    maxTanggal = 31
    namaBulan = "agustus"
elif(bulan == 9):
    maxTanggal = 30
    namaBulan = "september"
elif(bulan == 10):
    maxTanggal = 31
    namaBulan = "oktober"
elif(bulan == 11):
    maxTanggal = 30
    namaBulan = "november"
elif(bulan == 12):
    maxTanggal = 31
    namaBulan = "desember"

if(validTahun and kabisat and validBulan):
    if(tanggal <= maxTanggal):
        print(tanggal,namaBulan,tahun,y)
    else:
        print(tanggal,namaBulan,tahun,n)
elif(validTahun and validBulan):
    if(tanggal <= maxTanggal):
        print(tanggal,namaBulan,tahun,y)
    else:
        print(tanggal,namaBulan,tahun,n)
else:
    print(tanggal,bulan,tahun,n)