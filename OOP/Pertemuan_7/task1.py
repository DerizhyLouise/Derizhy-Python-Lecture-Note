class derizhy:
    listMHS = []
    
    def masukData(self):
        nm = ""
        nme = ""
        no = ""
        cek = True
        while cek:
            NIM = yield nm
            if len(self.listMHS) < 1: cek = False
            else:
                cek = False
                for i in range(len(self.listMHS)):
                    if self.listMHS[i]["NIM"] == NIM:
                        cek = True
                if cek:
                    print("Mahasiswa ini telah diabsen sebelumnya")
        nama = yield nme
        noHP = yield no
        temp = {"NIM": NIM, "Nama": nama, "Nomor HP": noHP}
        self.listMHS.append(temp)
    
    def absensi(self):
        print("="*47)
        print("Absensi Mahasiswa")
        for i in self.listMHS:
            for j in i: print(f"{j}: {i[j]}")
            print()
            
    def sort(self):
        self.listMHS = sorted(self.listMHS, key=lambda x: x['NIM'])
        
    def cariMHS(self, x):
        jumlah = 0
        print("="*47)
        for i in range(len(self.listMHS)):
            if x == self.listMHS[i].get('NIM'):
                print(f"Mahasiswa dengan NIM {x} ditemukan")
                for j in self.listMHS[i]: print(f"{j}: {self.listMHS[i][j]}")
                break
            jumlah += 1
        if jumlah == len(self.listMHS): print(f"Mahasiswa dengan NIM {x} tidak ditemukan")
            
mhs = derizhy()

'''
a = mhs.masukData()
next(a)
a.send(201110004)
a.send("Ada Apa")
a.send("08222134112")

b = mhs.masukData()
next(b)
b.send(201110004)
b.send(201110002)
b.send("Ada Ape")
b.send("08222134143")

c = mhs.masukData()
next(c)
c.send(201110005)
c.send("Ada Api")
c.send("08222134124")

d = mhs.masukData()
next(d)
d.send(201110003)
d.send("Ada Apo")
d.send("08222134126")

e = mhs.masukData()
next(e)
e.send(201110001)
e.send("Ada Apu")
e.send("08222134531")

mhs.absensi()
mhs.sort()
mhs.absensi()

mhs.cariMHS(201110006)
mhs.cariMHS(201110003)
mhs.cariMHS(201110000)
'''