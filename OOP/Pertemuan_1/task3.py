class les:
    def __init__(self, nama, tingkatan):
        if (tingkatan ==  "TK"):
            self.jam = "2 jam"
            self.biaya = "Rp. 300.000,00"
        elif (tingkatan == "SD"):
            self.jam = "2 jam"
            self.biaya = "Rp. 500.000,00"
        elif (tingkatan == "SMP"):
            self.jam = "1 jam"
            self.biaya = "Rp. 700.000,00"
        else:
            self.jam = "1 jam"
            self.biaya = "Rp. 1.000.000,00"
        self.nama = nama
        self.tingkatan = tingkatan
    
    def cetak(self):
        print("Kartu Private")
        print(f"Nama             = {self.nama}")
        print(f"Tingkatan        = {self.tingkatan}")
        print(f"Jam Pengajaran   = {self.jam}")
        print(f"Biaya les        = {self.biaya}")

a = les("Budi", "SMA")
b = les("Dina", "SD")

a.cetak()
print("\n")
b.cetak()