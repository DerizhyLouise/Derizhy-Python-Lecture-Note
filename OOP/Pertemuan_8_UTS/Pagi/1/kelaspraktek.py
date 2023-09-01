import kelasteori as kt

class kelas_praktek(kt.kelas_teori):
    def __init__(self, kode, nama, matkul, jlh):
        super().__init__(kode, nama, matkul, jlh)
            
    def cetak_kelas(self):
        print()
        print("Kode Kelas         = ", self.kode)
        print("Nama Kelas         = ", self.nama)
        print("Nama Mata Kuliah   = ", self.matkul)
        print("Jumlah Komputer    = ", self.jlh)