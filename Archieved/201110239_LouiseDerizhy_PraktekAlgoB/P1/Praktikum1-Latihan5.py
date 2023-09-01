print("Ini adalah program untuk menghitung nilai akhir mahasiswa")

x = float(input("Masukkan nilai tugas mahasiswa: "))
y = float(input("Masukkan nilai uts mahasiswa: "))
z = float(input("Masukkan nilai uas mahasiswa: "))

na = (0.3) * x + (0.3) * y + (0.4) * z

print("Nilai akhir mahasiswa adalah","%.2f" % na)