import LouiseDerizhy_201110239 as kelas

gudang1 = kelas.storage()
gudang1.produkMasuk(1, "Meja", 52)
gudang1.produkMasuk(2, "Kursi", 41)
gudang1.produkMasuk(3, "Lemari", 80)
gudang1.produkMasuk(4, "Sofa", 63)
gudang1.produkMasuk(5, "Kulkas", 21)
gudang1.produkMasuk(6, "Pintu", 45)
gudang1.produkMasuk(7, "Cermin", 87)
gudang1.produkMasuk(8, "Air Conditioner", 43)
gudang1.produkMasuk(9, "Kipas Angin", 22)
gudang1.produkMasuk(10, "Tempat Tidur", 67)

gudang1.tampilkanIsiGudang()
gudang1.sortirProduk()
gudang1.tampilkanIsiGudang()

gudang1.cariProduk(3)
gudang1.cariProduk(6)
gudang1.cariProduk(12)
