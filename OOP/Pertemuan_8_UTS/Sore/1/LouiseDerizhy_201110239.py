class storage:
    listProduk = []
    totalStok = 0
    
    def produkMasuk(self, kode, produk, stok):
        temp = {"Kode Produk": kode, "Nama Produk": produk, "Jumlah Stok": stok}
        self.listProduk.append(temp)
        self.totalStok += stok
        
    def sortirProduk(self):
        self.listProduk = sorted(self.listProduk, key=lambda x: x['Jumlah Stok'])
        print("Barang telah disortir berdasarkan jumlah stok")
    
    def cariProduk(self, x):
        print("="*45)
        print("Mencari produk dengan kode :", x)
        lenght = len(self.listProduk)
        y = 0
        for i in self.listProduk:
            if x == i["Kode Produk"]:
                print("Produk berhasil ditemukan!")
                print("Kode Produk  : ", i["Kode Produk"])
                print("Nama Produk  : ", i["Nama Produk"])
                print("Jumlah Stok  : ", i["Jumlah Stok"])
                print("="*45)
                break
            y+=1
        if y == lenght: 
            print("Produk tidak dapat ditemukan!")
            print("="*45)
        
    def tampilkanIsiGudang(self):
        print("="*45)
        print(f"Berikut adalah isi dari gudang\n")
        for i in self.listProduk:
            print("Kode Produk  : ", i["Kode Produk"])
            print("Nama Produk  : ", i["Nama Produk"])
            print("Jumlah Stok  : ", i["Jumlah Stok"])
            print()
        print(f"Jumlah total stok yang ada : {self.totalStok}")
        print("="*45)