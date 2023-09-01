class les:
    def __init__(self, nama, jenisKelamin, kelas, jenisLes):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.kelas = kelas
        self.jenisLes = jenisLes
        
    def cekNama(self):
        temp = self.nama.upper()
        spasi = " "
        try:
            for i in range(len(temp)):
                if (ord(temp[i]) < 65 or ord(temp[i]) > 90) and ord(temp[i]) != 32:
                    raise ValueError
            print("Nama telah valid\n")
            return True
        except:
            print("Nama hanya boleh terdiri dari spasi dan huruf saja\n")
            return False
            
    def cekGender(self):
        gender = self.jenisKelamin.lower()
        try:
            if gender != "laki-laki" and gender != "perempuan":
                raise ValueError
            print("Jenis kelamin telah valid\n")
            return True
        except: 
            print("Jenis kelamin tidak valid\n")
            return False
    
    def cekKelas(self):
        arr = ["SMA", "SMP", "SD", "TK"]
        temp = self.kelas.upper()
        jumlah = 0
        try:
            for i in range(len(arr)):
                if temp == arr[i]: 
                    print("Kelas sudah valid\n")
                    return True
                else: jumlah+=1
            if jumlah == 4: raise ValueError
        except: 
            print("Kelas tidak valid\n")
            return False
        
    def cekJenisLes(self):
        arr = ["mafia", "bahasa", "komputer", "umum"]
        temp = self.jenisLes.lower()
        jumlah = 0
        try:
            for i in range(len(arr)):
                if temp == arr[i]: 
                    print("Jenis les sudah valid\n")
                    return True
                else: jumlah+=1
            if jumlah == 4: raise ValueError
        except: 
            print("Jenis les tidak valid\n")
            return False
        
    def cetak(self):
        if self.cekNama() and self.cekGender() and self.cekJenisLes() and self.cekKelas():
            if self.kelas.upper() == "SMA": 
                biaya = 1000000
                jam = 1
            elif self.kelas.upper() == "SMP": 
                biaya = 700000
                jam = 1
            elif self.kelas.upper() == "SD": 
                biaya = 500000
                jam = 2
            else: 
                biaya = 300000
                jam = 2
            print("Kartu Les")
            print(f"Nama            : {self.nama}")
            print(f"Tingkatan       : {self.kelas}")
            print(f"Jam Pengajaran  : {jam}")
            print(f"Biaya Les       : Rp {biaya}")
        else: print("Data belum valid, silahkan lakukan validisasi data terlebih dahulu")
        
    
        
a = les("Shane", "Laki-laki", "SMA", "Mafia")
b = les("Jessica123", "Peremlakik", "SMK", "semua")
a.cetak()
b.cetak()
