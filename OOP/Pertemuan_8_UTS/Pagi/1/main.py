import kelasteori as kt
import kelaspraktek as kp

kelas1 = kt.kelas_teori("A0001", "Master", "Algoritma Pemrograman", 50)
kelas2 = kt.kelas_teori("A0002", "Giga", "PBO", 60)
kelas3 = kp.kelas_praktek("B0001", "Cyber1", "Algoritma Pemrograman", 50)
kelas4 = kp.kelas_praktek("B00021", "LOL", "PBO", 60)
kelas5 = kp.kelas_praktek("B0003", "Grey", "Rekayasa Data", 30)

list_kelas = [kelas1, kelas2, kelas3, kelas4, kelas5]

for i in list_kelas:
    i.cetak_kelas()
    print()
    i.cek_kode_kelas()
    i.cek_nama_kelas()
    i.cek_jumlah()