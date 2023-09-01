from abc import ABC, abstractmethod

class sortir:
    def __init__(self):
        self.jlhD = 0
        self.jlhM = 0

    def sort(self, x):
        z = False
        if x.__class__.__name__ == "dosen":
            z = True
            self.jlhD += 1/2
        else:
            self.jlhM += 1/2
        return z

class abst(ABC):
    @abstractmethod
    def hasil():
        pass

class mahasiswa:
    def __init__ (self, nim, nama, kelas, jurusan, jenisKelamin):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan
        self.jenisKelamin = jenisKelamin
        
    
class dosen:
    def __init__ (self, nip, nama, jabatan, jenisKelamin, noHP):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenisKelamin = jenisKelamin
        self.noHP = noHP
        
class absensi(abst):
    def hasil(self, x, y):
        if y.sort(x):
            print()
            print()
            print(f"NIP                  : {x.nip}")
            print(f"Nama                 : {x.nama}")
            print(f"Jabatan              : {x.jabatan}")
            print(f"Jenis Kelamin        : {x.jenisKelamin}")
            print(f"Nomor HP             : {x.noHP}")
        else :
            print()
            print()
            print(f"NIM                  : {x.nim}")
            print(f"Nama                 : {x.nama}")
            print(f"Kelas                : {x.kelas}")
            print(f"Jurusan              : {x.jurusan}")
            print(f"Jenis Kelamin        : {x.jenisKelamin}")
            
class jumlah(abst):
    def hasil(self, x, y):
        y.sort(x)
        print("-"*43)
        print("Dosen yang hadir     :", int(y.jlhD))
        print("Mahasiswa yang hadir :", int(y.jlhM))

class proses:
    def __init__(self):
        self.absensi = absensi()
        self.jumlah = jumlah()
        
    def tampilProses(self, x, y):
        self.absensi.hasil(x, y)
        self.jumlah.hasil(x, y)

class main:
    def __init__(self):
        self.li = []
        self.proses = proses()
        self.sortir = sortir()
    
    def tampil(self):
        for i in li:
            self.proses.tampilProses(i, self.sortir)
            
    def inputAbsen(self, x):
        self.li.append(x)

if __name__ == '__main__':    
    a = mahasiswa (201110239, "Louise Derizhy", "IF B_Sore", "Teknik Informatika", "Laki-laki")
    b = mahasiswa (201110240, "Kevin", "IF A_Sore", "Teknik Informatika", "Laki-laki")
    c = mahasiswa (201110241, "Vani", "IF B_Sore", "Teknik Informatika", "Perempuan")
    d = mahasiswa (201110242, "Rachel", "IF A_Sore", "Teknik Informatika", "Perempuan")
    e = dosen (1000100, "Michael", "Dosen", "Laki-laki", "085278329471")
    f = dosen (1000200, "Cleo", "Dosen", "Perempuan", "085278329472")
    li = [a,e,c,f,d,b]
    
    main = main()
    for i in li: main.inputAbsen(i)
    main.tampil()