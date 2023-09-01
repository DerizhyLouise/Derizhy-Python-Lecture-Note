class handSanitizer:
    def __init__(self, merek, stok):
        self.merek = merek
        self.stok = stok
    def cetak(self):
        print(f"Merek   = {self.merek}")
        print(f"Stok    = {self.stok} buah")
        
class banMobil:
    def __init__(self, merek, stok):
        self.merek = merek
        self.stok = stok
    def cetak(self):
        print(f"\nMerek   = {self.merek}")
        print(f"Stok    = {self.stok} buah")
        
class minumanBayi:
    def __init__(self, merek, stok):
        self.merek = merek
        self.stok = stok
    def cetak(self):
        print(f"\nMerek   = {self.merek}")
        print(f"Stok    = {self.stok} buah")

class buah:
    def __init__(self, nama, stok):
        self.nama = nama
        self.stok = stok
    def cetak(self):
        print(f"\nNama    = {self.nama}")
        print(f"Stok    = {self.stok} buah")

a = handSanitizer ("Santai", 10)
b = banMobil ("Yokomaha", 20)
c = minumanBayi ("Sipirit", 5)
d = buah ("Apel", 30)

a.cetak()
b.cetak()
c.cetak()
d.cetak()