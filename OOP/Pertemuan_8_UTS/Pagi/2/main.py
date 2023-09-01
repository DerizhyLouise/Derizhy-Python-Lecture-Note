import kelas

gudang = kelas.gudang()
gudang.masuk_barang(1, "Komputer", 52)
gudang.masuk_barang(2, "Ponsel", 41)
gudang.masuk_barang(3, "WIFI", 80)
gudang.masuk_barang(4, "Kabel", 63)
gudang.masuk_barang(5, "Keyboard", 21)

gudang.cetak()
gudang.sort()
gudang.cetak()

gudang.cari(3)
gudang.cari(6)
gudang.cari(5)
