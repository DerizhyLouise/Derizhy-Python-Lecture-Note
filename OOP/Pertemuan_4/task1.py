class kampus:
    def __init__(self, nama, noHP):
        self.nama = nama
        self.noHP = noHP

    def cekNama(self):
        temp = self.nama.upper()
        spasi = " "
        try:
            for i in range(len(temp)):
                if (ord(temp[i]) < 65 or ord(temp[i]) > 90) and ord(temp[i]) != 32:
                    raise ValueError
            print("Nama telah valid")
        except:
            print("Nama hanya boleh terdiri dari spasi dan huruf saja\n")
    
    def cekNoHP(self):
        temp = self.noHP
        try:
            for i in range(len(temp)):
                if (ord(temp[i]) < 48 or ord(temp[i]) > 57) and ord(temp[i]) != 43:
                    raise ValueError
            if len(temp) < 8 or len(temp) > 15: print("Panjang nomor telepon harus berada pada rentang 8 sampai dengan 15 angka saja\n")
            else: print("Nomor telepon telah valid\n")
        except:
            print("Nomor telepon hanya terdiri dari angka dan tanda tambah (+)\n")
                

class mahasiswa(kampus):
    def __init__(self, nama, noHP, NIM):
        super().__init__(nama, noHP)
        self.NIM = NIM
        
    def cekNIM(self):
        temp = self.NIM
        syarat = 9
        try:
            for i in range(len(temp)):
                x = int(temp[i])
            if syarat != len(temp): print("NIM harus memiliki panjang 9 karakter\n")
            else: print("NIM telah valid\n")
        except:
            print("NIM hanya boleh terdiri dari angka\n")
            

class dosen(kampus):
    def __init__(self, nama, noHP, NIP):
        super().__init__(nama, noHP)
        self.NIP = NIP  
              
    def cekNIP(self):
        temp = self.NIP
        syarat = 9
        try:
            for i in range(len(temp)):
                x = int(temp[i])
            if syarat != len(temp): print("NIP harus memiliki panjang 9 karakter\n")
            else: print("NIP telah valid\n")
        except:
            print("NIP hanya boleh terdiri dari angka\n")
        
a = mahasiswa("Louise#Derizhy", "+6282367319569", "201110239")
b = dosen("Manusia123", "+62899193213132wakwaw", "a20291223")
a.cekNama()
a.cekNIM()
a.cekNoHP()
b.cekNama()
b.cekNIP()
b.cekNoHP()