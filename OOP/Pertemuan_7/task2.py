class derizhy:
    listBrg = []
    
    def masukData(self):
        kd = ""
        mrk = ""
        jlh = 0
        cek = True
        while cek:
            kode = yield kd
            if len(self.listBrg) < 1: cek = False
            else:
                cek = False
                for i in range(len(self.listBrg)):
                    if self.listBrg[i]["Kode"] == kode:
                        cek = True
                if cek:
                    print("Kode produk ini telah digunakan sebelumnya")
                    print("Mohon input kode baru")
        merek = yield mrk
        jumlah = yield jlh
        temp = {"Kode": kode, "Jenis Produk": self.__class__.__name__, "Merek": merek, "Jumlah": jumlah}
        self.listBrg.append(temp)
        
class handSanitizer (derizhy):
    pass
        
class banMobil (derizhy):
    pass
        
class minumanBayi (derizhy):
    pass

class buah (derizhy):
    pass
        
class gudang:
    def __init__(self):
        self.listProduk = []
        self.stok = 0
        
    def barangMasuk(self, barang):
        self.listProduk.extend(barang)
        for i in self.listProduk:
            self.stok += i["Jumlah"]
        
    def cetakSemua(self):
        print("="*45)
        print("List Kode Barang")
        for i in self.listProduk:
            print("Kode Barang  : ", i["Kode"])
            print("Jenis Produk : ", i["Jenis Produk"])
            print("Merek        : ", i["Merek"])
            print("Jumlah Stok  : ", i["Jumlah"])
            print()
        print("="*45)
    
    def cetak(self, inKode):
        print("="*45)
        print(f"Mencari data dengan kode {inKode}...")
        temp = iter(self.listProduk)
        while True: 
            try:
                x = next(temp)
                if x["Kode"] == inKode: 
                    print("Data ditemukan!")
                    print("Kode Barang  : ", x["Kode"])
                    print("Nama Barang  : ", x["Jenis Produk"]) 
                    print("Merek        : ", x["Merek"]) 
                    print("Jumlah Stok  : ", x["Jumlah"])
                    if x["Jumlah"] < 10: print("Jumlah stok kurang!")
                    print("="*45)
                    break
            except StopIteration: 
                print(f"Data tidak ditemukan!") 
                print("="*45)
                break
            
    def sort(self):
        self.listProduk = sorted(self.listProduk, key=lambda x: x["Kode"])
        
    def jumlahStok(self):
        print("="*45)
        print(f"Jumlah stok yang ada di gudang : {self.stok}")

# Deklarasi
gudang = gudang()
a1 = handSanitizer()
a2 = handSanitizer()
b1 = minumanBayi()
b2 = minumanBayi()
c1 = buah()
c2 = buah()
d1 = banMobil()
d2 = banMobil()

'''
a1 = a1.masukData()
next(a1)
a1.send("A01")
a1.send("Sani A")
a1.send(20)

d2 = d2.masukData()
next(d2)
d2.send("D02")
d2.send("Ban Luar")
d2.send(11)   

c2 = c2.masukData()
next(c2)
c2.send("C02")
c2.send("Buah Asam")
c2.send(8)

b2 = b2.masukData()
next(b2)
b2.send("B02")
b2.send("Drinky B")
b2.send(30)

c1 = c1.masukData()
next(c1)
c1.send("C02")
c1.send("C01")
c1.send("Buah Manis")
c1.send(5)

a2 = a2.masukData()
next(a2)
a2.send("A02")
a2.send("Sani B")
a2.send(5)

d1 = d1.masukData()
next(d1)
d1.send("D01")
d1.send("Ban Dalam")
d1.send(6)

b1 = b1.masukData()
next(b1)
b1.send("B01")
b1.send("Drinky A")
b1.send(9)

gudang.barangMasuk(derizhy.listBrg)
gudang.cetakSemua()
gudang.sort()
gudang.cetakSemua()

gudang.cetak("A01")
gudang.cetak("A04")
gudang.cetak("C02")
gudang.jumlahStok()
'''