class derizhy:
    def __init__(self, nim, nama, noHP):
        self.nim = nim
        self.nama = nama
        self.noHP = noHP
    
    @classmethod
    def masukData(cls):
        while True:
            try: 
                nim = input("Masukkan NIM      : ")
                for i in range(len(nim)):
                    if (ord(nim[i]) < 48 or ord(nim[i]) > 57) or len(nim) != 9: raise ValueError
                break
            except: print("NIM wajib terdiri dari 9 angka")
        while True:
            spasi = " "
            try:
                nama = input("Masukkan Nama     : ")
                temp = nama.upper()
                for i in range(len(temp)):
                    if (ord(temp[i]) < 65 or ord(temp[i]) > 90) and ord(temp[i]) != 32:
                        raise ValueError
                break
            except: print("Nama hanya boleh terdiri dari spasi dan huruf saja")
        while True:
            try:
                noHP = input("Masukkan Nomor HP : ")
                for i in range(len(noHP)):
                    if ord(noHP[i]) < 48 or ord(noHP[i]) > 57: raise ValueError
                if len(noHP) < 8 or len(noHP) > 15: print("Panjang nomor telepon harus berada pada rentang 8 sampai dengan 15 angka saja")
                else: break
            except:
                print("Nomor telepon hanya terdiri dari angka")
        print("="*40)
        return cls(nim, nama, noHP)
    
    def absensi(mhsList, cek):
        temp = len(mhsList)
        jumlah = 0
        for i in mhsList:
            if i.nim == cek: 
                print("Mahasiswa ditemukan")
                print(f"NIM         : {i.nim}")
                print(f"Nama        : {i.nama}")
                print(f"Nomor HP    : {i.noHP}")
                break
            jumlah += 1
        if temp == jumlah: print(f"Mahasiswa dengan NIM {cek} tidak ditemukan")
        print("="*40)
        

mhs1 = derizhy.masukData()
mhs2 = derizhy.masukData()
mhs3 = derizhy.masukData()
mhs4 = derizhy.masukData()
mhs5 = derizhy.masukData()
mhsList = [mhs1, mhs2, mhs3, mhs4, mhs5]
derizhy.absensi(mhsList, "201110001")
derizhy.absensi(mhsList, "201110004")
derizhy.absensi(mhsList, "201110006")