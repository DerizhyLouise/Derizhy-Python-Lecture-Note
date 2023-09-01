class gudang:
    list_brg = []
    
    def masuk_barang(self, kode, nama_brg, stok):
        temp = {"kode": kode, "nama barang": nama_brg, "stok": stok}
        self.list_brg.append(temp)
        
    def sort(self):
        self.list_brg = sorted(self.list_brg, key=lambda x: x['stok'])
        print("Barang telah di sortir berdasarkan jumlah stok")
        print()
    
    def cari(self, x):
        print("Mencari barang dengan kode barang :", x)
        temp = len(self.list_brg)
        j = 0
        for i in self.list_brg:
            if x == i["kode"]:
                print("Barang ditemukan!")
                print("Kode barang  : ", i["kode"])
                print("Nama barang  : ", i["nama barang"])
                print("Jumlah stok  : ", i["stok"])
                print()
                break
            j+=1
        if j == temp: 
            print("Barang tidak ditemukan")
            print()
        
    def cetak(self):
        for i in self.list_brg:
            print("Kode barang  : ", i["kode"])
            print("Nama barang  : ", i["nama barang"])
            print("Jumlah stok  : ", i["stok"])
            print()