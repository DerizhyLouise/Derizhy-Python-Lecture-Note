class derizhy:
    listMHS = []
    
    def masukData(self, NIM, nama, noHP):
        temp = {"NIM": NIM, "Nama": nama, "Nomor HP": noHP}
        self.listMHS.append(temp)
    
    def absensi(self):
        print("="*40)
        print("Absensi Mahasiswa")
        for i in self.listMHS:
            for j in i: print(f"{j}: {i[j]}")
            print()
            
    def sort(self):
        self.listMHS = sorted(self.listMHS, key=lambda x: x['NIM'])
        
    def cariMHS(self, x):
        jumlah = 0
        print("="*40)
        for i in range(len(self.listMHS)):
            if x == self.listMHS[i].get('NIM'):
                print(f"Mahasiswa dengan NIM {x} ditemukan")
                for j in self.listMHS[i]: print(f"{j}: {self.listMHS[i][j]}")
                break
            jumlah += 1
        if jumlah == len(self.listMHS): print(f"Mahasiswa dengan NIM {x} tidak ditemukan")
            
mhs = derizhy()
mhs.masukData(201110004, "Ada Apa", "08222134112")
mhs.masukData(201110002, "Ade Ape", "08222134123")
mhs.masukData(201110005, "Adi Api", "08222134143")
mhs.masukData(201110003, "Ado Apo", "08222134175")
mhs.masukData(201110001, "Adu Apu", "08222134114")

mhs.absensi()
mhs.sort()
mhs.absensi()

mhs.cariMHS(201110006)
mhs.cariMHS(201110003)
mhs.cariMHS(201110000)