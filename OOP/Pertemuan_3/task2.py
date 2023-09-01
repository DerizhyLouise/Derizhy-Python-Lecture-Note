from abstract import syaratTask2

class les:
    def __init__(self, nama, noHP):
        self.nama = nama
        self.noHP = noHP
        
class sma (les, syaratTask2):
    nama = ""
    noHP = ""
    def __init__(self, nama, noHP, jenisKelas):
        super().__init__(nama, noHP)
        self.jenisKelas = jenisKelas
        
    def biayaLes (self):
        print(f"Biaya les {self.nama} : Rp 1.200.000,00\n")
        
class smp (les, syaratTask2):
    nama = ""
    noHP = ""
    def __init__(self, nama, noHP, umur):
        super().__init__(nama, noHP)
        self.umur = umur
        
    def biayaLes (self):
        print(f"Biaya les {self.nama} : Rp 800.000,00\n")
        
class sd (les, syaratTask2):
    nama = ""
    noHP = ""
    def __init__(self, nama, noHP, jenisKelamin):
        super().__init__(nama, noHP)
        self.jenisKelamin = jenisKelamin
        
    def biayaLes (self):
        print(f"Biaya les {self.nama} : Rp 500.000,00\n")

a = sd ("Angel", "082273218423", "Perempuan")
b = sd ("Budi", "082671628362", "Laki-laki")
c = sd ("Charles", "089726317236", "Laki-laki")
d = smp ("Dina", "086251726329", 14)
e = smp ("Elvi", "086251723517", 15)
f = sma ("Fiona", "086251824621", "IPA")
g = sma ("Gerry", "087812361237", "IPS")
h = sma ("Harry", "089212378321", "IPA")

a.biayaLes()
b.biayaLes()
c.biayaLes()
d.biayaLes()
e.biayaLes()
f.biayaLes()
g.biayaLes()
h.biayaLes()