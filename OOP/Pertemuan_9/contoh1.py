class BUKU:
    def __init__(self, nama, tahun, jlh):
        self.nama = nama
        self.tahun = tahun
        self.jlh = jlh
    
    def cetakBuku(self):
        hasil = "Nama Buku = {}\n".format(self.nama)
        hasil += "Tahun Buku = {}\n".format(self.tahun)
        hasil += "Jumlah Buku = {}\n".format(self.jlh)
        return hasil

class cekTahun(BUKU):
    def __init__(self, proses):
        self._proses = proses
    def cetakBuku(self):
        thn = 2021
        hasil = self._proses.cetakBuku()
        hasil += "Buku termasuk buku {}\n".format("Baru" if (thn - self._proses.tahun) < 5 else "Lama")
        return hasil

class cekStok(BUKU):
    def __init__(self, proses):
        self._proses = proses
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        hasil += "Perlu {}\n".format("Mencari Buku" if self._proses.jlh < 3 else "Mencari Pembaca")
        return hasil

if __name__ == '__main__':
    buku1 = BUKU("Pemrograman Python", 2019, 3)
    denganCekTahun = cekTahun(buku1)
    denganCekJumlah = cekStok(buku1)
    denganCekSemua = cekStok(cekTahun(buku1))

    print("Awal :\n", buku1.cetakBuku())
    print()
    print("Dengan Cek Tahun:\n", denganCekTahun.cetakBuku())
    print()
    print("Dengan Cek Jumlah:\n", denganCekJumlah.cetakBuku())
    print()
    print("Dengan Cek Semua:\n", denganCekSemua)