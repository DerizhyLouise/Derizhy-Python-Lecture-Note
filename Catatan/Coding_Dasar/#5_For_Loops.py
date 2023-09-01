# for
# List sebagai Iterable

gorengan = ("Bakwan","Pisang Goreng","Tahu Isi","Kue Sayur")

for g in gorengan:
    print(g)
    print(len(g))
    
# String sebagai Iterable
bakwan = "Bakwan"

for b in bakwan:
    print(b)
    
# For di dalam for
gorengan = ("Bakwan","Pisang Goreng","Tahu Isi","Kue Sayur")
sayuran = ("Kol","Wortel","Daun Ubi","Bayam")
buah = ("Apel","Pisang","Nanas","Semangka")

daftar_belanja = (gorengan,sayuran,buah)

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)
        
buah = ("Apel","Pisang","Nanas","Semangka","Nangka","Jeruk","Pepaya")
beli = "Nanas"

if beli in buah:
    print("Penjual : \"Ya saya jual",beli,"\b\"")
if not beli in buah:
    print("Penjual : \"Saya tidak jual",beli,"\b\"")

# Atau lebih mudah, if not diganti menjadi else

# for range, break
number = 25

for i in range(0,40):
    print(i)
    if i is number:
        print("Angka ditemukan",i)
        break # Menghentikan segala tindakan
    
else:
    print("Angka tidak ditemukan")
print("Space diluar for")

# for continue
print("\n")

for i in range(1,10):
    if i is 6:
        print("Nilai i adalah",6)
        continue # Melanjutkan ke step berikutnya
        print("Cek 1")
    print("Nilai saat ini adalah",i)
else:
    print("Akhir dari loop")

# for pass
print("\n")

for i in range(1,10):
    if i is 6:
        print("Nilai i adalah",6)
        pass # Melewati / Pass
        print("Cek 1")
    print("Nilai saat ini adalah",i)
else:
    print("Akhir dari loop")
