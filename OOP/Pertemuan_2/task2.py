class andre:
    def __init__(self, merek, jumlah, hargaModal):
        self.merek = merek
        self.jumlah = jumlah
        self.hargaModal = hargaModal
        
class handSanitizer (andre):
    def __init__(self, merek, jumlah, hargaModal, isi):
        super().__init__(merek, jumlah, hargaModal)
        self.isi = isi
    def laporan (self):
        print("Pengeluaran Hand Sanitizer")
        print(f"Merek       : {self.merek}")
        print(f"Isi         : {self.isi} Liter")
        print(f"Jumlah      : {self.jumlah}")
        print(f"Harga Modal : Rp {self.hargaModal}")
        print(f"Pengeluaran : Rp {self.hargaModal * self.jumlah}")
        print("\n")
        
class banMobil (andre):
    def __init__(self, merek, jumlah, hargaModal, warna):
        super().__init__(merek, jumlah, hargaModal)
        self.warna = warna
    def laporan (self):
        print("Pengeluaran Ban Mobil")
        print(f"Merek       : {self.merek}")
        print(f"Warna       : {self.warna}")
        print(f"Jumlah      : {self.jumlah}")
        print(f"Harga Modal : Rp {self.hargaModal}")
        print(f"Pengeluaran : Rp {self.hargaModal * self.jumlah}")
        print("\n")
        
class minumanBayi (andre):
    def __init__(self, merek, jumlah, hargaModal, isi):
        super().__init__(merek, jumlah, hargaModal)
        self.isi = isi
    def laporan (self):
        print("Pengeluaran Minuman Bayi")
        print(f"Merek       : {self.merek}")
        print(f"Isi         : {self.isi} Liter")
        print(f"Jumlah      : {self.jumlah}")
        print(f"Harga Modal : Rp {self.hargaModal}")
        print(f"Pengeluaran : Rp {self.hargaModal * self.jumlah}")
        print("\n")

class buah (andre):
    def __init__(self, merek, jumlah, hargaModal, nama):
        super().__init__(merek, jumlah, hargaModal)
        self.nama = nama
    def laporan (self):
        print("Pengeluaran Buah")
        print(f"Nama Buah   : {self.nama}")
        print(f"Merek       : {self.merek}")
        print(f"Jumlah      : {self.jumlah}")
        print(f"Harga Modal : Rp {self.hargaModal}")
        print(f"Pengeluaran : Rp {self.hargaModal * self.jumlah}")
        print("\n")
        
a = handSanitizer("Santai", 10, 50000, 5)
b = handSanitizer("Bersih", 20, 60000, 3)
c = banMobil("Yokohama", 30, 200000, "Hitam")
d = banMobil("Yokohama", 30, 200000, "Putih")
e = minumanBayi("Okezone", 20, 15000, 2)
f = minumanBayi("Not Okezone", 25, 17000, 1)
g = buah("Happy Fruit", 30, 25000, "Apel") 
h = buah("Happy Fruit", 40, 18000, "Jeruk") 

a.laporan()
b.laporan()
c.laporan()
d.laporan()
e.laporan()
f.laporan()
g.laporan()
h.laporan()