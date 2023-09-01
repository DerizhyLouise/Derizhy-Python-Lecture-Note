print("Berikut adalah program konversi waktu")

det = int(input("Masukkan nilai detik: "))

jam = det / 3600
detik = det % 60
det = det // 60
menit = det % 60

print("Hasil:", int(jam),"jam", int(menit), "menit", int(detik), "detik")