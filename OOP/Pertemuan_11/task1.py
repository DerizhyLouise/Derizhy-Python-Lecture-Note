class derizhy:
    def __init__(self, dosen):
        self.kelas = ""
        self.proses = ""
        self.jumlah = 0
        self.dosen = dosen
    
    def absen(self):
        self.jumlah += 1
        
    def cetakKelas(self):
        print("Ini adalah", self.__class__.__name__)
        print("Yang merupakan kelas", self.kelas)
        
    def cetakDosen(self):
        print("Dosen Pengajar :", self.dosen)
        
    def cetakProses(self):
        print(self.proses)
        
    def cetakJumlah(self):
        print(f"Jumlah mahasiswa yang hadir : {self.jumlah} orang")
    
class Kelas_A(derizhy):
    def __init__(self, dosen):
        self.kelas = "T1/L2"
        self.proses = "Kelas ini mempelajari tentang\nperhitungan kalkulus dan prosesnya"
        self.jumlah = 0
        self.dosen = dosen

class Kelas_B(derizhy):
    def __init__(self, dosen):
        self.kelas = "T3/L2"
        self.proses = "Kelas ini mempelajari pemrograman\nbeserta proses-prosesnya"
        self.jumlah = 0
        self.dosen = dosen

class Kelas_C(derizhy):
    def __init__(self, dosen):
        self.kelas = "T5/L2"
        self.proses = "Kelas ini mempelajari Bahasa Inggris\ndan formula-formula pembuatan katanya"
        self.jumlah = 0
        self.dosen = dosen
        
class rekapAbsensi:
    def __init__(self):
        self.li = []
        
    def masuk(self, kelas):
        self.li.append(kelas)
    
    def rekap(self):
        for i in self.li:
            print("="*41)
            print("==============REKAP ABSENSI==============")
            print("="*41)
            i.cetakKelas()
            i.cetakDosen()
            i.cetakProses()
            i.cetakJumlah()
        
if __name__ == '__main__':
    a = Kelas_A("Anderson")
    b = Kelas_B("Beny")
    c = Kelas_C("Charlie")
    
    # Proses absensi
    for i in range(55):
        a.absen()
    for i in range(57):
        b.absen()
    for i in range(54):
        c.absen()
        
    # Proses Rekap Absensi
    x = rekapAbsensi()
    x.masuk(a)
    x.masuk(b)
    x.masuk(c)
    x.rekap()