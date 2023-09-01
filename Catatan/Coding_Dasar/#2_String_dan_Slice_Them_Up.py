data = "Ini adalah String"
print(data)
print(type(data))

# Cara membuat String

# 1. Dengan menggunakan Quote
'''
    1. Dengan menggunakan Single Quote '...'
    2. Dengan menggunakan Double Quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan dobule quote"
print(data)

print('"Halo apa kabar?"')
print("'Halo apa kabar?'")
print("Ini adalah hari Jum'at")

# 2. Dengan menggunakan tanda \

# Membuat tanda ' menjadi string
print('It\'s a good day, isn\'t it?')

# Backlash
print("C:\\ucup\\Ucup")

# Tab
print("Hello \tworld!!!")

# Backspace
print("Hello \bworld!!!")

# Newline
print("Ini baris pertama.\nIni baris kedua.") # LF -> Line Feed
print("Ini baris pertama.\rIni baris kedua.") # CR -> Carriage Return
print("Ini baris pertama.\n\rIni baris kedua") # CRLF -> Line Feed Carriage Return

# 3. String Literal atau raw

# Hati-hati
print("C:\newfolder") # Akan salah pathnya

# Menggunakan raw string
print(r"C:\newfolder")

# Multiline Literal String
print("""
Nama : Orang
Kelas : 5 SD
""")

# Multiline Literal String and raw
print(r"""
Nama : Orang
Kelas : 5 SD
Website : www.orang.com/newID
""")

# Slice Them Up

Data = "Pisang Goreng"
a = Data[0]
b = Data[2]
c = Data[4]
d = Data[0:3]
e = Data[2:6]
f = Data[-1]
g = Data[-3]
h = Data[1:-3]
i = Data[-8:-4]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
