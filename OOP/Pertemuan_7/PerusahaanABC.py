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
        while True:
            try:
                masuk = int(input("Jumlah barang masuk : "))
                break
            except:
                print("Mohon masukkan angka!")
        self.jumlah += masuk
        print(f"Jumlah stok sekarang : {self.jumlah}\n")

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
        
class gudang:
    
    def __init__(self):
        self.listProduk = []
        
    def produkMasuk(self, produk):
        self.listProduk.append(produk)
        
    def produkKeluar(self, inKode):
        print("="*35)
        print("Produk Keluar")
        temp = iter(self.listProduk)
        while True: 
            try:
                x = next(temp)
                if x.kode == inKode: 
                    x.cekKode()
                    x.barangKeluar()
                    break
            except StopIteration: 
                print(f"Data tidak ditemukan!") 
                break
            
    def cekStok(self):
        for i in self.listProduk:
            print("="*40)
            while i.jumlah < 10:
                i.cekKode()
                print("Jumlah stok kurang!")
                yield i.barangMasuk()
        
a = komputer(101, "Apple", 5, "8GB", "544GB", "I5")
b = router(401, "Router Keren", 17, "5Mbps")
c = kabelJaringan(201, "Kabel A", 9, "5M", "Hitam")
d = switch(501, "Siwtc", 10, "Ya")
e = accessPoint(301, "Access A", 20, "Ya")
f = komputer(102, "ASUS", 8, "8GB", "544GB", "I5")
g = router(402, "Router Jelek", 7, "10Mbps")
h = accessPoint(302, "Access B", 20, "Tidak")
i = switch(502, "Siw", 1, "Tidak")
j = kabelJaringan(202, "Kabel B", 17, "6M", "Putih")
temp = [a, b, c, d, e, f, g, h, i, j]
gudang = gudang()
for i in temp:
    gudang.produkMasuk(i)
for i in gudang.cekStok():
    pass
gudang.produkKeluar(101)