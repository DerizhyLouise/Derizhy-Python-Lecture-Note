import kelasinduk as ki

class kelasPraktek(ki.kelasTeori):
    def __init__(self, kodeKelas, namaKelas, mataKuliah, jumlah):
        super().__init__(kodeKelas, namaKelas, mataKuliah, jumlah)
            
    def cetakKelas(self):
        print()
        print("Kode Kelas         = ", self.kodeKelas)
        print("Nama Kelas         = ", self.namaKelas)
        print("Nama Mata Kuliah   = ", self.mataKuliah)
        print("Jumlah Komputer    = ", self.jumlah)