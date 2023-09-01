def inputBuku(self): 
    kd = ""
    nm = "" 
    jns = "" 
    cek = True 
    while cek: 
        kodeBuku = yield kd 
        if(self.perpus < 1): cek = False 
        else: 
            cek = False 
            for i in range(len(self.perpus)): 
                if(self.perpus[i]['kode'] == kodeBuku): 
                    cek = True 
            if(cek): 
                print("Kode Buku sudah terdaftar ... !!!") 
                print("Masukkan kode buku lagi ... !!!") 
    namaBuku = yield nm 
    jenisBuku = yield jns 
    tmp = {"kode" : kodeBuku, "nama" : namaBuku, "jenis" : jenisBuku} 
    self.perpus.append(tmp)