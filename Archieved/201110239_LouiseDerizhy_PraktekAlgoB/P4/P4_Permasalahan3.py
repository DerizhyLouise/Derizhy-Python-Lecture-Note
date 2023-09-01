print("Berikut adalah program untuk menentukan jumlah dan Rata dari masukan")

n = int(input("Masukkan banyak angka yang akan diinput: "))

total = 0

for i in range(n):
    x = int(input("Masukkan angka: "))
    total += x 

rata = total / n
print(total,"%.3f"%rata)