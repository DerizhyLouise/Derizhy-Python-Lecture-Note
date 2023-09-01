class derizhy:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        
    def cetakBarang(self):
        print(f"Jenis Produk : {self.__class__.__name__}")
        print(f"Kode Barang  : {self.kode}")
        print(f"Merek        : {self.merek}")
        print(f"Jumlah Stok  : {self.jumlah}")
        print()
        
class handSanitizer (derizhy):
    def __init__(self, kode, merek, jumlah):
        super().__init__(kode, merek, jumlah)
        
class banMobil (derizhy):
    def __init__(self, kode, merek, jumlah):
        super().__init__(kode, merek, jumlah)
        
class minumanBayi (derizhy):
    def __init__(self, kode, merek, jumlah):
        super().__init__(kode, merek, jumlah)

class buah (derizhy):
    def __init__(self, kode, merek, jumlah):
        super().__init__(kode, merek, jumlah)
        
class gudang:
    def __init__(self):
        self.list = []
    
    def barangMasuk(self, barang):
        self.list.append(barang)
        
    def cetakSemua(self):
        print("="*35)
        print("List Kode Barang")
        for i in self.list:
            derizhy.cetakBarang(i)
        print("="*35)
    
    def cetak(self, inKode):
        print("="*35)
        print(f"Mencari data dengan kode {inKode}...")
        temp = iter(self.list)
        while True: 
            try:
                x = next(temp)
                if x.kode == inKode: 
                    print("Data ditemukan!")
                    print(f"Kode Barang  : {x.kode}") 
                    print(f"Merek        : {x.merek}") 
                    print(f"Jumlah Stok  : {x.jumlah}")
                    if x.jumlah < 10: print("Jumlah stok kurang!")
                    print("="*35)
                    break
            except StopIteration: 
                print(f"Data tidak ditemukan!") 
                print("="*35)
                break
            
    def sort(self):
        self.list = sorted(self.list, key=lambda x: x.kode)

gudang = gudang()
a1 = handSanitizer("A01", "Sani A", 20)
a2 = handSanitizer("A02", "Sani B", 5)
b1 = minumanBayi("B01", "Drinky A", 9)
b2 = minumanBayi("B02", "Drinky B", 30)
c1 = buah("C01", "Buah Manis", 5)
c2 = buah("C02", "Buah Asam", 8)
d1 = banMobil("D01", "Ban Dalam", 6)
d2 = banMobil("D02", "Ban Luar", 11)

listBarang = [c1, d1, b1, d2, a1, b2, a2, c2]
for i in listBarang:
    gudang.barangMasuk(i)
    
gudang.cetakSemua()
gudang.sort()
gudang.cetakSemua()

gudang.cetak("A01")
gudang.cetak("A04")
gudang.cetak("C02")