class mahasiswa:
    jumlahM = 0
    
    def __init__ (self, nim, nama, kelas, jurusan, jenisKelamin):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan
        self.jenisKelamin = jenisKelamin
        mahasiswa.jumlahM += 1
        
    def cetakM(self):
        print("\nAbsensi Mahasiswa")
        print(f"NIM              = {self.nim}")
        print(f"Nama             = {self.nama}")
        print(f"Kelas            = {self.kelas}")
        print(f"Jurusan          = {self.jurusan}")
        print(f"Jenis Kelamin    = {self.jenisKelamin}")
        
    def hadirM():
        print("\nJumlah Mahasiswa yang hadir : ", mahasiswa.jumlahM)
    
class dosen:
    jumlahD = 0
    
    def __init__ (self, nip, nama, jabatan, jenisKelamin, noHP):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenisKelamin = jenisKelamin
        self.noHP = noHP
        dosen.jumlahD += 1
            
    def cetakD(self):
        print("\nAbsensi Dosen")
        print(f"NIP              = {self.nip}")
        print(f"Nama             = {self.nama}")
        print(f"Jabatan          = {self.jabatan}")
        print(f"Jenis Kelamin    = {self.jenisKelamin}")
        print(f"Nomor HP         = {self.noHP}")

    def hadirD():
        print("Jumlah Dosen yang hadir : ", dosen.jumlahD)
        
a = mahasiswa (201110239, "Louise Derizhy", "IF B_Sore", "Teknik Informatika", "Laki-laki")
b = mahasiswa (201110240, "Kevin", "IF A_Sore", "Teknik Informatika", "Laki-laki")
c = mahasiswa (201110241, "Vani", "IF B_Sore", "Teknik Informatika", "Perempuan")
d = mahasiswa (201110242, "Rachel", "IF A_Sore", "Teknik Informatika", "Perempuan")
e = dosen (1000100, "Michael", "Dosen", "Laki-laki", "085278329471")
f = dosen (1000200, "Cleo", "Dosen", "Perempuan", "085278329472")

a.cetakM()
b.cetakM()
c.cetakM()
d.cetakM()
e.cetakD()
f.cetakD()

mahasiswa.hadirM()
dosen.hadirD()