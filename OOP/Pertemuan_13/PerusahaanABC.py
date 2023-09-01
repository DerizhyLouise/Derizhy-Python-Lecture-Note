class produk:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        
    def cetak(self):
        print(f"Produk  : {self.__class__.__name__}")
        print(f"Kode    : {self.kode}")
        print(f"Merek   : {self.merek}")
        print(f"Jumlah  : {self.jumlah}\n")

class Komputer(produk):
    def __init__(self, kode, merek, jumlah, ram, memory, GPU):
        super().__init__(kode, merek, jumlah)
        self.ram = ram
        self.memory = memory
        self.GPU = GPU
        
class Kabel_Jaringan(produk):
    def __init__(self, kode, merek, jumlah, panjang, warna):
        super().__init__(kode, merek, jumlah)
        self.panjang = panjang
        self.warna = warna
        
class gudang:
    def __init__(self):
        self.listProduk = []
        
    def produkMasuk(self, produk):
        self.listProduk.append(produk)
        
    def cek (self, x):
        y = 0
        for i in range(len(self.listProduk)):
            if self.listProduk[i].kode == x:
                self.listProduk[i].cetak()
                return self.listProduk[i].kode
                break
            else:
                y += 1
            if y == len(self.listProduk):
                print(f"Produk dengan kode {x} tidak ditemukan")

a = Komputer(4, "Lenovo", 15, "4GB", "128GB", "i5")
b = Komputer(15, "Acer", 25, "8GB", "128GB", "i5")
c = Kabel_Jaringan(5, "Kabel D", 11, "3M", "Hitam")
d = Komputer(14, "Asus", 45, "16GB", "1TB", "i7")
e = Kabel_Jaringan(11, "Kabel A", 23, "5M", "Hitam")
f = Komputer(7, "Asus", 15, "8GB", "522GB", "i3")
g = Komputer(12, "Apple", 30, "8GB", "522GB", "i5") 
h = Komputer(10, "Mac Book", 50, "16B", "522GB", "i7") 
i = Kabel_Jaringan(2, "Kabel B", 35, "2M", "Putih")
j = Komputer(6, "Acer", 5, "8GB", "224GB", "i5") 
k = Kabel_Jaringan(9, "Kabel C", 74, "2M", "Merah")
l = Komputer(3, "Asus", 12, "8GB", "1TB", "i3") 
m = Komputer(8, "Toshiba", 32, "8GB", "522GB", "i5") 
n = Komputer(1, "Apple", 33, "8GB", "128GB", "i7")
o = Kabel_Jaringan(13, "Kabel E", 28, "5M", "Biru")
barang = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
gudang1 = gudang()
for i in range(len(barang)):
    gudang1.produkMasuk(barang[i])