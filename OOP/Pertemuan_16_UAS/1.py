from abc import ABC, abstractmethod

class sembakoLouise(ABC):
    def __init__(self, kode, nama, harga, exp, jlh):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.exp = exp
        self.jlh = jlh
        
    def cetak(self):
        print("="*45)
        print(f"Jenis Produk    : {self.__class__.__name__}")
        print(f"Kode Produk     : {self.kode}")
        print(f"Nama Produk     : {self.nama}")
        print(f"harga Produk    : {self.harga}")
        print(f"Tanggal Expired : {self.exp}")
        print(f"Jumlah          : {self.jlh}")
        print("="*45)

class Beras(sembakoLouise):
    def __init__(self, kode, nama, harga, exp, jlh):
        super().__init__(kode, nama, harga, exp, jlh)
    
class Gula(sembakoLouise):
    def __init__(self, kode, nama, harga, exp, jlh):
        super().__init__(kode, nama, harga, exp, jlh)
        
class produk:
    def __init__(self):
        self.listProduk = []
        
    def masuk(self, produk):
        self.listProduk.append(produk)
        
    def cari(self, x):
        y = 0
        for i in range(len(self.listProduk)):
            if self.listProduk[i].kode == x:
                print("Produk ditemukan!")
                self.listProduk[i].cetak()
                return self.listProduk[i].kode
                break
            else:
                y += 1
            if y == len(self.listProduk):
                print(f"Produk dengan kode {x} tidak ditemukan")    

class menu:
    def __init__(self):
        self.produk = produk()
    
    def operate(self):
        while True:
            print()
            print("Selamat datang di Sembako Louise")
            print("1 - Masuk Produk")
            print("2 - Cari Produk")
            print("3 - Cetak Semua Produk")
            print("4 - Keluar")
            while True:
                try:
                    x = int(input("Masukkan perintah (1/2/3/4): "))
                    if x > 4 or x < 1:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Perintah tidak valid!")
            
            if x == 1:
                while True:
                    print("Pilih produk yang akan dimasukkan")
                    print("1 - Beras")
                    print("2 - Gula")
                    print("3 - Batal masukkan produk")
                    while True:
                        try:
                            y = int(input("Masukkan perintah (1/2/3): "))
                            if y > 3 or y < 1:
                                raise ValueError
                            else:
                                break
                        except ValueError:
                            print("Perintah tidak valid!")
                    if y == 1:
                        kode = int(input("Kode          : "))
                        nama = input("Nama          : ")
                        harga = int(input("Harga         : "))
                        exp = input("Expired       : ")
                        jlh = int(input("Jumlah        : "))
                        produk = Beras(kode, nama, harga, exp, jlh)
                        self.produk.masuk(produk)
                        print("Berhasil memasukkan produk!")
                        print()
                    elif y == 2:
                        kode = int(input("Kode          : "))
                        nama = input("Nama          : ")
                        harga = int(input("Harga         : "))
                        exp = input("Expired       : ")
                        jlh = int(input("Jumlah        : "))
                        produk = Gula(kode, nama, harga, exp, jlh)
                        self.produk.masuk(produk)
                        print("Berhasil memasukkan produk!")
                    else:
                        print("Kembali ke menu utama...")
                        print("="*40)
                        print()
                        break
                    
            elif x == 2:
                cariKode = int(input("Masukkan kode produk yang dicari : "))
                self.produk.cari(cariKode)
            
            elif x == 3:
                for i in self.produk.listProduk:
                    i.cetak()
                    
            else:
                print("Selamat tinggal!")
                break
     
if __name__ == '__main__':
    menu = menu()
    menu.operate()
    
'''
--READ ME--
Mohon untuk copy data di bawah ini untuk memasukkan data dengan cepat
Setelah run file python, langsung paste dan menekan enter

1
1
1
Beras A
50000
17 Januari 2023
15
1
2
Beras B
60000
18 Januari 2023
20
2
3
Gula A
15000
19 Mei 2022
14
2
4 
Gula B
17000
20 Juni 2022
19
3
'''