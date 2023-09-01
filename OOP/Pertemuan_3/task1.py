from abstract import syaratTask1

class kampus:
    def __init__(self, nomorInduk, nama, gender, noHP):
        self.nomorInduk = nomorInduk
        self.nama = nama
        self.gender = gender
        self.noHP = noHP

class mhs (kampus, syaratTask1):
    nomorInduk = ""
    nama = ""
    gender = ""
    noHP = ""
    def __init__(self, nomorInduk, nama, gender, noHP, jurusan, kelas):
        super().__init__(nomorInduk, nama, gender, noHP)
        self.jurusan = jurusan
        self.kelas = kelas
        
    def cetakData (self):
        print(f"Terima kasih sudah hadir {self.nama}\n")
        
class dosen (kampus, syaratTask1):
    nomorInduk = ""
    nama = ""
    gender = ""
    noHP = ""
    def __init__(self, nomorInduk, nama, gender, noHP):
        super().__init__(nomorInduk, nama, gender, noHP)
        
    def cetakData (self):
        print(f"Silahkan mulai pelajaran Pak/Bu {self.nama}\n")
        
a = mhs(201110239,"Louise Derizhy","Laki-laki","082367319569", "Teknik Informatika", "IF_B Sore")
b = mhs (201110240, "Kevin", "Laki-laki", "082163182361", "Teknik Informatika", "IF_A Sore")
c = mhs (201110241, "Vani", "Perempuan", "086281672821", "Teknik Informatika", "IF_B Sore")
d = mhs (201110242, "Rachel", "Perempuan", "082617238212", "Teknik Informatika", "IF_A Sore")
e = dosen (1000100, "Michael", "Laki-laki", "085278329471")
f = dosen (1000200, "Cleo", "Perempuan", "085278329472")
a.cetakData()
b.cetakData()
c.cetakData()
d.cetakData()
e.cetakData()
f.cetakData()