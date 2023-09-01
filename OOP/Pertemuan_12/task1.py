from abc import ABC, abstractmethod
# Menggunakan Composite Pattern

class mendaftar:
    def __init__(self, nama, gender, usia):
        self.nama = nama
        self.gender = gender
        self.usia = usia
        self.biaya = biayaTotal()
        
    def cetakProses(self):
        print("Memulai proses pendaftaran...")
        print(f"Nama                : {self.nama}")
        print(f"Jenis Kelamin       : {self.gender}")
        print(f"Usia                : {self.usia} tahun")
        print()
        print("Mengkalkulasikan total biaya pendaftaran...")
        print(f"Biaya Pendaftaran   : Rp {self.biaya.returnBiaya()}")
        print("Terima kasih telah mendaftar :)")
        print("="*45)

class biaya:
    @abstractmethod
    def returnBiaya(self):
        pass
    
class biayaTotal(biaya):
    def __init__(self):
        self.uangPendaftaran = uangPendaftaran()
        self.uangKuliahPertama = uangKuliahPertama()
        self.uangMPT = uangMPT()
    
    def returnBiaya(self):
        x = self.uangPendaftaran.returnBiaya()
        y = self.uangKuliahPertama.returnBiaya()
        z = self.uangMPT.returnBiaya()
        return x + y + z

class uangPendaftaran(biaya):
    def __init__(self):
        self.biaya = 200000
    
    def returnBiaya(self):
        return self.biaya
    
class uangKuliahPertama(biaya):
    def __init__(self):
        self.biaya = 1500000
    
    def returnBiaya(self):
        return self.biaya
    
class uangMPT(biaya):
    def __init__(self):
        self.uangTraining = 100000
        self.uangPenginapan = 200000
        self.uangKonsumsi = 150000
    
    def returnBiaya(self):
        return self.uangTraining + self.uangKonsumsi + self.uangPenginapan

if __name__ == '__main__':
    #Proses mendaftar
    a = mendaftar("Louise Derizhy", "Laki-laki", 19)
    b = mendaftar("Subjek 1", "Perempuan", 20)
    c = mendaftar("Subjek 2", "Laki-laki", 18)
    li = [a, b, c]
    
    for i in li:
        i.cetakProses()