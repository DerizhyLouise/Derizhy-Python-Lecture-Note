# Input dan Output File

'''
w = write mode / mode menulis dan menghapus file lama
r = read mode / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
'''

# Membuat file text
file = open("data.txt","w") # Jika ada file bernama data.txt sebelumnya, maka file tersebut akan dihapus dan digantikan dengan file baru

file.write("Ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nIni adalah baris kedua")
file.write("\nIni adalah baris ketiga")
file.write("\nIni adalah baris keempat")
file.write("\nIni adalah baris kelima")

file.close()

# Membaca file text

file1 = open("data.txt","r")

print(file1.read()) # file2.read(jumlah karakter yang ingin ditampilkan)

print(file1.readline()) # adalah cara untuk menampilkan per baris

file.close()

# Appending mode

file2 = open("data.txt","a")

file2.write("\nBaris ini dibuat menggunakan mode append")

file.close()