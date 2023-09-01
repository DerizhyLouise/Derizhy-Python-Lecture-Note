from abc import ABC, abstractmethod

class discount(ABC):
    def disc(self, jlhDisc):
        pass

class custNormal(discount):
    def __init__(self, nama):
        self.nama = nama
        self.membership = False
        
    def disc(self, jlhDisc):
        if self.membership == False:
            jlhDisc = 0
        return jlhDisc

class custLoyal(discount):
    def __init__(self, nama):
        self.nama = nama
        self.membership = True
        
    def disc(self, jlhDisc):
        if self.membership == False:
            jlhDisc = 0
        return jlhDisc

class produk:
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
        
    def cetak(self):
        print(f"Produk  : {self.__class__.__name__}")
        print(f"Kode    : {self.kode}")
        print(f"Merek   : {self.merek}")
        print(f"Jumlah  : {self.jumlah}\n")
        
    def beli(self, cust, produkID, jlh):
        for i in self.listProduk:
            if i.kode == produkID:
                if i.jumlah < jlh:
                    print("Stok produk kurang")
                    break
                else: i.jumlah -= jlh
                total = i.harga * jlh - (jlh * cust.disc(50000))
                print("="*45)
                print(f"Pembeli     : {cust.nama}")
                print(f"Produk      : {i.__class__.__name__}")
                print(f"Merek       : {i.merek}")
                print(f"Harga       : {i.harga}")
                print(f"Jumlah      : {jlh}")
                print(f"Total Harga : {total}")
                print("="*45)
        
class Komputer(produk):
    def __init__(self, kode, merek, jumlah, harga, ram, memory, GPU):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        self.harga = harga
        self.ram = ram
        self.memory = memory
        self.GPU = GPU
        
class Kabel_Jaringan(produk):
    def __init__(self, kode, merek, jumlah, harga, panjang, warna):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        self.harga = harga
        self.panjang = panjang
        self.warna = warna
        
if __name__ == '__main__':
    a = Komputer(1, "Lenovo", 15, 1000000, "4GB", "128GB", "i5")
    b = Kabel_Jaringan(2, "Kabel D", 11, 50000, "3M", "Hitam")
    c = Komputer(3, "Asus", 45, 20000000, "16GB", "1TB", "i7")
    d = Kabel_Jaringan(4, "Kabel A", 23, 55000, "5M", "Hitam")
    barang = [a, b, c, d]
    gudang = produk()
    for i in range(len(barang)):
        gudang.produkMasuk(barang[i])
        
    cust1 = custLoyal("Levi")
    cust2 = custNormal("Angel")
    
    gudang.beli(cust1, 3, 2)
    gudang.beli(cust2, 2, 4)