def kali(a,b):
    c = a*b
    return c

hasil = kali(3,4)
print(hasil)

# Perintah di atas dapat dibuat lebih simpel dengan lambda
# Membuat anonymous function dengan lambda
kali = lambda x,y: x*y
hasil = kali(3,4)
print(hasil)