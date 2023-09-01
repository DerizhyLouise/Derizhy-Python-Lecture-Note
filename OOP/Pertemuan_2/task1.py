class derizhy:
    def __init__(self, nomorInduk, nama, gender, noHP):
        self.nomorInduk = nomorInduk
        self.nama = nama
        self.gender = gender
        self.noHP = noHP

class mhs (derizhy):
    def __init__(self, nomorInduk, nama, gender, noHP, jurusan, kelas):
        super().__init__(nomorInduk, nama, gender, noHP)
        self.jurusan = jurusan
        self.kelas = kelas
    def absensi (self):
        print(f"Nomor Induk   : {self.nomorInduk}")
        print(f"Nama          : {self.nama}")
        print("\n")
        
class dosen (derizhy):
    def __init__(self, nomorInduk, nama, gender, noHP):
        super().__init__(nomorInduk, nama, gender, noHP)
    def perkenalan (self):
        print(f"Nama          : {self.nama}")
        print(f"Nomor HP      : {self.noHP}")
        print("\n")
        
a = mhs(201110239,"Louise Derizhy","Laki-laki","082367319569", "Teknik Informatika", "IF_B Sore")
b = mhs (201110240, "Kevin", "Laki-laki", "082163182361", "Teknik Informatika", "IF_A Sore")
c = mhs (201110241, "Vani", "Perempuan", "086281672821", "Teknik Informatika", "IF_B Sore")
d = mhs (201110242, "Rachel", "Perempuan", "082617238212", "Teknik Informatika", "IF_A Sore")
e = dosen (1000100, "Michael", "Laki-laki", "085278329471")
f = dosen (1000200, "Cleo", "Perempuan", "085278329472")
a.absensi()
b.absensi()
c.absensi()
d.absensi()
e.perkenalan()
f.perkenalan()