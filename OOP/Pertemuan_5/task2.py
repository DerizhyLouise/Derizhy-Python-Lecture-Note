class derizhy:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
        
    @classmethod
    def masukData(cls):
        print("="*30)
        return cls(
            int(input("Masukkan Kode    : ")),
            input("Masukkan Merek   : "),
            int(input("Masukkan Jumlah  : "))
        )
        
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
    
    def cetak(self, inKode):
        temp = iter(self.list)
        while True: 
            try:
                x = next(temp)
                if x.kode == inKode: 
                    print("="*30)
                    print("Data ditemukan!")
                    print(f"Kode Barang  : {x.kode}") 
                    print(f"Merek        : {x.merek}") 
                    print(f"Jumlah Stok  : {x.jumlah}")
                    if x.jumlah < 10: print("Jumlah stok kurang!")
                    print("="*30)
                    break
            except StopIteration: 
                print("="*30)
                print(f"Kode tidak ditemukan!") 
                print("="*30)
                break

gudang = gudang()
a = handSanitizer.masukData()
b = minumanBayi.masukData()
c = buah.masukData()
d = banMobil.masukData()
e = buah.masukData()

gudang.barangMasuk(a)
gudang.barangMasuk(b)
gudang.barangMasuk(c)
gudang.barangMasuk(d)
gudang.barangMasuk(e)
gudang.cetak(2)
gudang.cetak(3)
gudang.cetak(6)