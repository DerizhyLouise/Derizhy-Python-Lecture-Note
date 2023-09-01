Data = [1,4,9,16,25,36,49,64]
'''
() merupakan tuple, artinya list yang di dalam tuple tidak dapat diubah lagi
Gunakan [] agar list masih dapat diubah-ubah
'''

# Mengakses List
Subdata1 = Data[3]
Subdata2 = Data[-3]
print(Subdata1)
print(Subdata2)

# Memotong list
Subdata3 = Data[2:4]
Subdata4 = Data[:4]
print(Subdata3)
print(Subdata4)

Data2 = [100,200,300,400,500,600,700,800]
# Menambah List
Data3 = Data + Data2
print(Data3)

# Merubah Content dari List
Data[4] = 87
print(Data)

# Mengcopy List ke Variable baru
a = Data [:]
a[7] = 87
print(a)
print(Data)

# Merubah Content List dengan Menggungakan Metode Slicing
Data[3:5] = [11,12]
print(Data)

# List dalam List
x = [Data,Data2]
print(x)

# Mengakses List dalam Multidimensional List
y = x[1][4]
print(y)

# Methods untuk List
Data.append(30)

# Function yang bisa kita gunakan kepada List
panjang_list = len(Data)
print(Data)
print(panjang_list)

print("\n")
# Memanipulasi List
barang = ["Meja","Buku","Pensil","Penghapus","Penggaris"]
print(barang)

# Beberapa Method yang dapat digunakan untuk manipulasi list
# Method untuk menambahkan sesuatu ke dalam list
barang.append("Kursi")
print(barang)
stuff = barang.copy() # Untuk membuat list tersendiri
print("\n1")
stuff.append("Laptop")
print(stuff)
print(barang)
print("\n1")

barang.extend("Botol")
print(barang)

barang.insert(3,"Kursi")
print(barang)

# Method untuk menghitung anggota
jumlahKursi = barang.count("Kursi")
print("Jumlah kursi adalah",jumlahKursi)

# Method untuk menghapus data
barang.remove("Kursi") # Menghapus data tertentu
print(barang)

barang.pop() # Menghapus data terbaru
print(barang)

# Method untuk mereverse data
barang.reverse()
print(barang)
