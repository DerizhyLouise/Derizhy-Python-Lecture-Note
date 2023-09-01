import kelasinduk as ki
import kelasturunan as kt

kelas1 = ki.kelasTeori("T1", "Relativity", "Algoritma Pemrograman", 50)
kelas2 = ki.kelasTeori("T2", "Velocity", "Struktur Diskit", 60)
kelas3 = ki.kelasTeori("T3", "Area", "Matematika Komputer", 55)
kelas4 = ki.kelasTeori("T4", "Acceleration", "Pemrograman Berbasis Objek", 60)
kelas5 = ki.kelasTeori("T6", "Gravitation", "Rekayasa Data", 50)
kelas6 = kt.kelasPraktek("P1", "Hydrogen", "Algoritma Pemrograman", 50)
kelas7 = kt.kelasPraktek("P2", "Oxygen", "Pemrograman Berbasis Objek", 60)
kelas8 = kt.kelasPraktek("P3", "Helium", "Back End", 55)
kelas9 = kt.kelasPraktek("P4", "Carbon", "Otomasi Perkantoran", 60)
kelas10 = kt.kelasPraktek("P5", "Natrium", "Front End", 55)

list_kelas = [kelas1, kelas2, kelas3, kelas4, kelas5, kelas6, kelas7, kelas8, kelas9, kelas10]

for i in list_kelas:
    i.cetakKelas()
    print()