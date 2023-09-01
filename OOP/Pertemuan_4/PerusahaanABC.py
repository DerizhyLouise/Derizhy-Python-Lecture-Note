class produk:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        
    def cekKode(self):
        print(f"Kode    : {self.kode}")
        print(f"Merek   : {self.merek}")
        print(f"Jumlah  : {self.jumlah}\n")
    
    def barangKeluar(self):
        while True:
            keluar = int(input("Jumlah barang keluar : "))
            self.jumlah -= keluar
            if self.jumlah > 0:
                print(f"Jumlah stok yang tersisa : {self.jumlah}\n")
                break
            else:
                print("Jumlah stok kurang")
                self.jumlah += keluar
        
    def barangMasuk(self):
        masuk = int(input("Jumlah barang masuk : "))
        self.jumlah += masuk
        print(f"Jumlah stok sekarang : {self.jumlah}\n")
    
    def cekStok(self):
        print(f"Jumlah stok : {self.jumlah}")
        while self.jumlah < 10:
            try:
                print("Jumlah stok di bawah aturan")
                print("Silahkan masukkan barang")
                self.barangMasuk()
            except:
                print("Jumlah stok masih kurang")

class komputer(produk):
    def __init__(self, kode, merek, jumlah, ram, memory, GPU):
        super().__init__(kode, merek, jumlah)
        self.ram = ram
        self.memory = memory
        self.GPU = GPU

class kabelJaringan(produk):
    def __init__(self, kode, merek, jumlah, panjang, warna):
        super().__init__(kode, merek, jumlah)
        self.panjang = panjang
        self.warna = warna

class accessPoint(produk):
    def __init__(self, kode, merek, jumlah, wireless):
        super().__init__(kode, merek, jumlah)
        self.wireless = wireless
        
class router(produk):
    def __init__(self, kode, merek, jumlah, kecepatan):
        super().__init__(kode, merek, jumlah)
        self.kecepatan = kecepatan
        
class switch(produk):
    def __init__(self, kode, merek, jumlah, managable):
        super().__init__(kode, merek, jumlah)
        self.managable = managable

a = komputer(1, "LG", 15, "5GB", "12GB", "i5")
a.cekKode()
a.barangMasuk()
a.barangKeluar()
a.cekStok()