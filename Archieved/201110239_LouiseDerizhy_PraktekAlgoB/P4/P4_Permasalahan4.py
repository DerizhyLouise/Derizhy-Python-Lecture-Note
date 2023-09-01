print("Berikut adalah program untuk menghitung jumlah dan rata-rata")

angka = []
angka = list(map(int,input().split()))
total = sum(angka)
rata = total / len(angka)

print(total,"%.3f"%rata)