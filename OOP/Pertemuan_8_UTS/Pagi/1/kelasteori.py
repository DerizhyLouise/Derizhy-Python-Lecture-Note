class kelas_teori:
    
    def __init__(self, kode, nama, matkul, jlh):
        self.kode = kode
        self.nama = nama
        self.matkul = matkul
        self.jlh = jlh
        
    def cek_kode_kelas(self):
        temp = self.kode
        try:
            if len(temp) != 5: raise ValueError
            for i in range(len(temp)):
                if (ord(temp[i]) < 65 or ord(temp[i]) > 90) and (ord(temp[i]) > 47 or ord(temp[i]) < 58):
                    raise ValueError
            print("Kode kelas telah benar")
        except:
            print("Kode kelas hanya terdiri dari huruf kapital dan angka dengan panjang 5 karakter!\n")
    
    def cek_nama_kelas(self):
        temp = self.nama.upper()
        try:
            for i in range(len(temp)):
                if (ord(temp[i]) < 65 or ord(temp[i]) > 90):
                    raise ValueError
            print("Nama kelas telah benar")
        except:
            print("Nama kelas hanya terdiri dari huruf saja\n")
    
    def cek_jumlah(self):
        try:
            if type(self.jlh) != int: raise ValueError
            else: print("Jumlah kursi telah benar\n")
        except:
            print("Jumlah kursi harus angka\n")
            
    def cetak_kelas(self):
        print()
        print("Kode Kelas         = ", self.kode)
        print("Nama Kelas         = ", self.nama)
        print("Nama Mata Kuliah   = ", self.matkul)
        print("Jumlah Kursi       = ", self.jlh)