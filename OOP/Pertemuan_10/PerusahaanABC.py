class produk:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
    
    # Template Pattern Method
    def cekSemua(self):
        self.cetak()
        self.cekJumlah()
        self.cekSpesifikasi()
        
    def cetak(self):
        print("="*45)
        print(f"Nama Produk     : {self.__class__.__name__}")
        print(f"Kode            : {self.kode}")
        print(f"Merek           : {self.merek}")
    
    def cekJumlah(self):
        print(f"Jumlah          : {self.jumlah}")
        if self.jumlah > 10: print("(Jumlah stok telah berlebihan!)")
        else: print("(Jumlah stok masih dibatas aman)")
    
    def cekSpesifikasi(self): pass
        
class Komputer(produk):
    def __init__(self, kode, merek, jumlah, ram, memory, GPU, kodePembuatan):
        super().__init__(kode, merek, jumlah)
        self.ram = ram
        self.memory = memory
        self.GPU = GPU
        self.kodePembuatan = kodePembuatan
        
    def cekSpesifikasi(self):
        print("Spesifikasi Produk")
        print(f"RAM             : {self.ram}")
        print(f"Memory          : {self.memory}")
        print(f"GPU             : {self.GPU}")
        print(f"Kode Pembuatan  : {self.kodePembuatan}")
        
class Kabel_Jaringan(produk):
    def __init__(self, kode, merek, jumlah, panjang, warna):
        super().__init__(kode, merek, jumlah)
        self.panjang = panjang
        self.warna = warna
        
    def cekSpesifikasi(self):
        print("Spesifikasi Produk")
        print(f"Panjang         : {self.panjang} meter")
        print(f"Warna           : {self.warna}")
        
class Access_Point(produk):
    def __init__(self, kode, merek, jumlah, wireless):
        super().__init__(kode, merek, jumlah)
        self.wireless = wireless
        
    def cekSpesifikasi(self):
        print("Spesifikasi Produk")
        print(f"Wirelss         : {self.wireless}")
        
class Router(produk):
    def __init__(self, kode, merek, jumlah, kecepatan):
        super().__init__(kode, merek, jumlah)
        self.kecepatan = kecepatan
        
    def cekSpesifikasi(self):
        print("Spesifikasi Produk")
        print(f"Kecepatan       : {self.kecepatan}")
        
class Switch(produk):
    def __init__(self, kode, merek, jumlah, managable):
        super().__init__(kode, merek, jumlah)
        self.managable = managable
        
    def cekSpesifikasi(self):
        print("Spesifikasi Produk")
        print(f"Managable       : {self.managable}")

if __name__ == '__main__':
    a = Komputer(101, "Apple", 5, "8GB", "544GB", "I5", "F-112")
    b = Router(401, "Router Keren", 17, "5Mbps")
    c = Switch(501, "Siwtc", 10, "Ya")
    d = Access_Point(301, "Access A", 20, "Ya")
    e = Kabel_Jaringan(202, "Kabel B", 4, 6, "Putih")
    li = [a, b, c, d, e]
    for i in li:
        i.cekSemua()