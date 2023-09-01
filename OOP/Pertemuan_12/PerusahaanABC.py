class produk:
    def __init__(self, kode, merek, jumlah):
        self.kode = kode
        self.merek = merek
        self.jumlah = jumlah
    
    def cekSemua(self):
        self.cetak()
        self.cekSpesifikasi()
        self.proses()
    
    def cetak(self):
        print("="*40)
        print(f"\t\tNama Produk     : {self.__class__.__name__}")
        print(f"\t\tKode            : {self.kode}")
        print(f"\t\tMerek           : {self.merek}")
        
class Komputer(produk):
    def __init__(self, kode, merek, jumlah, ram, memory, GPU, kodePembuatan):
        super().__init__(kode, merek, jumlah)
        self.ram = ram
        self.memory = memory
        self.GPU = GPU
        self.kodePembuatan = kodePembuatan
        
    def cekSpesifikasi(self):
        print("\t\tSpesifikasi Produk")
        print(f"\t\tRAM             : {self.ram}")
        print(f"\t\tMemory          : {self.memory}")
        print(f"\t\tGPU             : {self.GPU}")
        print(f"\t\tKode Pembuatan  : {self.kodePembuatan}")
        
    def proses(self):
        print("\t\tDeskripsi       :")
        print("\t\tKomputer dapat memproses algoritma")
        
class Kabel_Jaringan(produk):
    def __init__(self, kode, merek, jumlah, panjang, warna):
        super().__init__(kode, merek, jumlah)
        self.panjang = panjang
        self.warna = warna
        
    def cekSpesifikasi(self):
        print("\t\tSpesifikasi Produk")
        print(f"\t\tPanjang         : {self.panjang} meter")
        print(f"\t\tWarna           : {self.warna}")
        
    def proses(self):
        print("\t\tDeskripsi       :")
        print("\t\tKabel jaringan dapat menghubungkan\n\t\tdua perangkat")
        
class Access_Point(produk):
    def __init__(self, kode, merek, jumlah, wireless):
        super().__init__(kode, merek, jumlah)
        self.wireless = wireless
        
    def cekSpesifikasi(self):
        print("\t\tSpesifikasi Produk")
        print(f"\t\tWireless        : {self.wireless}")
        
    def proses(self):
        print("\t\tDeskripsi       :")
        print("\t\tAccess point untuk memancarkan\n\t\tsinyal internet")
        
class Router(produk):
    def __init__(self, kode, merek, jumlah, kecepatan):
        super().__init__(kode, merek, jumlah)
        self.kecepatan = kecepatan
        
    def cekSpesifikasi(self):
        print("\t\tSpesifikasi Produk")
        print(f"\t\tKecepatan       : {self.kecepatan}")
        
    def proses(self):
        print("\t\tDeskripsi       :")
        print("\t\tRouter menghubungkan berbagai\n\t\tjaringan sekaligus")
        
class Switch(produk):
    def __init__(self, kode, merek, jumlah, managable):
        super().__init__(kode, merek, jumlah)
        self.managable = managable
        
    def cekSpesifikasi(self):
        print("\t\tSpesifikasi Produk")
        print(f"\t\tManagable       : {self.managable}")
        
    def proses(self):
        print("\t\tDeskripsi       :")
        print("\t\tSwitch menghubungkan perangkat komputer")
        
class Smart_Phone(produk):
    def __init__(self, kode, merek, jumlah, ram, kamera):
        super().__init__(kode, merek, jumlah)
        self.ram = ram
        self.kamera = kamera
        
    def cekSpesifikasi(self):
        print("\t\tSpesifikasi Produk")
        print(f"\t\tRAM            : {self.ram}")
        print(f"\t\tKamera         : {self.kamera}")
        
    def proses(self):
        print("\t\tDeskripsi       :")
        print("\t\tSmart Phone merupakan komputer portable")
        
class compositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []
        
    def add(self, child):
        self.children.append(child)
        
    def remove(self, child):
        self.children.remove(child)
    
    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()
            
class leafElement:
    def __init__(self, *args):
        self.position = args[0]
    
    def showDetails(self):
        print("\t", end="")
        self.position.cekSemua()

if __name__ == '__main__':
    a = Komputer(101, "Apple", 5, "8GB", "544GB", "I5", "F-112")
    b = Router(401, "Router Keren", 17, "5Mbps")
    c = Switch(501, "Siwtc", 10, "Ya")
    d = Access_Point(301, "Access A", 20, "Ya")
    e = Kabel_Jaringan(202, "Kabel B", 4, 6, "Putih")
    f = Smart_Phone(601, "Samsul", 6, "6GB", "5MP")
    
    subMenuItem1 = compositeElement("Jaringan")
    subMenuItem11 = leafElement(b)
    subMenuItem12 = leafElement(c)
    subMenuItem13 = leafElement(d)
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem1.add(subMenuItem13)
    
    subMenuItem2 = compositeElement("Penghubung")
    subMenuItem21 = leafElement(a)
    subMenuItem22 = leafElement(e)
    subMenuItem23 = leafElement(f)
    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem23)
    
    topLevelMenu = compositeElement("Perusahaan ABC")
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()