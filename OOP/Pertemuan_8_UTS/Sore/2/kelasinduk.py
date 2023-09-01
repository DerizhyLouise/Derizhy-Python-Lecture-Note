class kelasTeori:
    def __init__(self, kodeKelas, namaKelas, mataKuliah, jumlah):
        self.kodeKelas = kodeKelas
        self.namaKelas = namaKelas
        self.mataKuliah = mataKuliah
        self.jumlah = jumlah
            
    def cetakKelas(self):
        print()
        print("Kode Kelas         = ", self.kodeKelas)
        print("Nama Kelas         = ", self.namaKelas)
        print("Nama Mata Kuliah   = ", self.mataKuliah)
        print("Jumlah Kursi       = ", self.jumlah)