class produk:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        
    def cekKode(self):
        print(f"Kode    : {self.kode}")
        print(f"Merek   : {self.merek}")
        print(f"Jumlah  : {self.jumlah}\n")
        
    def cek (x, z):
        temp = []
        y = []
        for i in range(len(x)):
            if str(x[i].__class__.__name__) == z:
                y.append(x[i])
        for i in range(len(y)-1):
                for j in range(i+1, len(y)):
                    if y[i].kode >= y[j].kode:
                        temp = y[i]
                        y[i] = y[j]
                        y[j] = temp
        print("List untuk", z)
        for i in y:
            i.cekKode()
        print("="*30)

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

a = komputer(4, "Lenovo", 15, "4GB", "128GB", "i5")
b = komputer(15, "Acer", 25, "8GB", "128GB", "i5")
c = kabelJaringan(5, "Kabel D", 11, "3M", "Hitam")
d = komputer(14, "Asus", 45, "16GB", "1TB", "i7")
e = kabelJaringan(11, "Kabel A", 23, "5M", "Hitam")
f = komputer(7, "Asus", 15, "8GB", "522GB", "i3")
g = komputer(12, "Apple", 30, "8GB", "522GB", "i5") 
h = komputer(10, "Mac Book", 50, "16B", "522GB", "i7") 
i = kabelJaringan(2, "Kabel B", 35, "2M", "Putih")
j = komputer(6, "Acer", 5, "8GB", "224GB", "i5") 
k = kabelJaringan(9, "Kabel C", 74, "2M", "Merah")
l = komputer(3, "Asus", 12, "8GB", "1TB", "i3") 
m = komputer(8, "Toshiba", 32, "8GB", "522GB", "i5") 
n = komputer(1, "Apple", 33, "8GB", "128GB", "i7")
o = kabelJaringan(13, "Kabel E", 28, "5M", "Biru")
barang = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
produk.cek(barang, "komputer")
produk.cek(barang, "kabelJaringan")