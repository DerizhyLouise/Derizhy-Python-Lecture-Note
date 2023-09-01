class mahasiswa:
    def __init__ (self, nim, nama, kelas, jurusan, jenisKelamin):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan
        self.jenisKelamin = jenisKelamin
        
    def cetakM(self):
        print("\nAbsensi Mahasiswa")
        print(f"NIM              = {self.nim}")
        print(f"Nama             = {self.nama}")
        print(f"Kelas            = {self.kelas}")
        print(f"Jurusan          = {self.jurusan}")
        print(f"Jenis Kelamin    = {self.jenisKelamin}")
    
class dosen:
    def __init__ (self, nip, nama, jabatan, jenisKelamin, noHP):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenisKelamin = jenisKelamin
        self.noHP = noHP
            
    def cetakD(self):
        print("\nAbsensi Dosen")
        print(f"NIP              = {self.nip}")
        print(f"Nama             = {self.nama}")
        print(f"Jabatan          = {self.jabatan}")
        print(f"Jenis Kelamin    = {self.jenisKelamin}")
        print(f"Nomor HP         = {self.noHP}")
        
class absensi:
    def __init__(self):
        self.jumlahMHS = 0
        self.jumlahDosen = 0
        self.li = []
    
    def hadir(self, x):
        self.li.append(x)
        if x.__class__.__name__ == "dosen": self.jumlahDosen += 1
        else: self.jumlahMHS += 1
        
    def jlhM(self):
        return self.jumlahMHS
    
    def jlhD(self):
        return self.jumlahDosen

a = mahasiswa (201110239, "Louise Derizhy", "IF B_Sore", "Teknik Informatika", "Laki-laki")
b = mahasiswa (201110240, "Kevin", "IF A_Sore", "Teknik Informatika", "Laki-laki")
c = mahasiswa (201110241, "Vani", "IF B_Sore", "Teknik Informatika", "Perempuan")
d = mahasiswa (201110242, "Rachel", "IF A_Sore", "Teknik Informatika", "Perempuan")
e = dosen (1000100, "Michael", "Dosen", "Laki-laki", "085278329471")
f = dosen (1000200, "Cleo", "Dosen", "Perempuan", "085278329472")
li = [a,b,c,d,e,f]

absensi = absensi()
for i in li:
    absensi.hadir(i)