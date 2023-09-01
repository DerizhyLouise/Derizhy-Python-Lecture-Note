class derizhy:
    def __init__(self, nama, gender, noHP):
        self.nama = nama
        self.gender = gender
        self.noHP = noHP
        
class mhs(derizhy):
    def __init__(self, NIM, nama, gender, noHP, jurusan):
        super().__init__(nama, gender, noHP)
        self.NIM = NIM
        self.jurusan = jurusan
        
    def absen(self):
        hasil = "Mahasiswa\n" 
        hasil += "NIM                : {}\n".format(self.NIM)
        hasil += "Nama               : {}\n".format(self.nama)
        hasil += "Jenis Kelamin      : {}\n".format(self.gender)
        hasil += "Nomor HP           : {}\n".format(self.noHP)
        hasil += "Jurusan            : {}\n".format(self.jurusan)
        return hasil
        
class dosen(derizhy):
    def __init__(self, NIP, nama, jabatan, gender, noHP):
        super().__init__(nama, gender, noHP)
        self.NIP = NIP
        self.jabatan = jabatan
        
    def absen(self):
        hasil = "Dosen\n" 
        hasil += "NIP                : {}\n".format(self.NIP)
        hasil += "Nama               : {}\n".format(self.nama)
        hasil += "Jabatan            : {}\n".format(self.jabatan)
        hasil += "Jenis Kelamin      : {}\n".format(self.gender)
        hasil += "Nomor HP           : {}\n".format(self.noHP)
        return hasil
        
class absensi(derizhy):
    def __init__(self):
        self.li = []
        self.jumlah = 0
        
    def masuk(self, data):
        self.li.append(data)
        self.jumlah += 1
        
    def cetak(self):
        print("=================ABSENSI=================\n")
        for i in li:
            print(i.absen())
        print("Jumlah Pengunjung = ", self.jumlah)
        
    def cari(self, x):
        print("="*39)
        print("Mencari Mahasiswa / Dosen")
        print("dengan Nomor Induk ", x)
        temp = iter(self.li)
        while True:
            try:
                y = next(temp)
                if y.__class__.__name__ == "dosen":
                    if y.NIP == x:
                        print("Dosen ditemukan!\n")
                        print(y.absen())
                        break
                elif y.__class__.__name__ == "mhs":
                    if y.NIM == x:
                        print("Mahasiswa ditemukan!\n")
                        print(y.absen())
                        break
            except StopIteration: 
                print(f"Nomor Induk {x} tidak ditemukan!") 
                break

if __name__ == '__main__':
    mhs1 = mhs(201110004, "Ada Apa", "Laki-laki", "08222134112", "Teknik Informatika")
    mhs2 = mhs(201110002, "Ade Ape", "Perempuan", "08222134123", "Teknik Informatika")
    mhs3 = mhs(201110005, "Adi Api", "Laki-laki", "08222134143", "Teknik Informatika")
    mhs4 = mhs(201110003, "Ado Apo", "Laki-laki", "08222134175", "Teknik Informatika")
    mhs5 = mhs(201110001, "Adu Apu", "Perempuan", "08222134114", "Teknik Informatika")
    dsn1 = dosen(100000001, "Dos Santa", "Dosen Backend", "Perempuan", "08222147284")
    dsn2 = dosen(100000002, "Dos Santo", "Dosen Backend", "Laki-laki", "08222147232")
    dsn3 = dosen(100000003, "Dos Sante", "Dosen Backend", "Perempuan", "08222145421")
    li = [mhs1, mhs2, dsn1, dsn3, mhs3, mhs4, mhs5, dsn2]
    absensi = absensi()
    for i in li: absensi.masuk(i)
    absensi.cetak()
    absensi.cari(201110005)
    absensi.cari(201110007)
    absensi.cari(100000003)