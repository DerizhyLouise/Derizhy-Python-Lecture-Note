class Ojek():
    
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
        
    def cekID(self):
        print("Nama: ",self.nama,"\nMotor: ",self.transmisi,"\nDaerah: ",self.daerah)

class Gojek(Ojek): # Class Inheritance menurunkan class sebelumnya ke class baru
    
    def cekID(self): # Kita juga dapat mengubah fungsi dari turunan class inheritance
        print("Cek di website")
        
ojek1 = Ojek("Mario","Manual","Bandung")
ojek2 = Gojek("Bambang","Automatic","Jakarta")

ojek1.cekID()
ojek2.cekID()