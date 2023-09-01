# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # adalah assignment
print("Nilai a =",a)

# Operasi Aritmatika
a += 1
print("Nilai a += 1, nilai a menjadi",a)

a -= 2
print("Nilai a -= 2, nilai a menjadi",a)

a *= 2
print("Nilai a *= 2, nilai a menjadi",a)

a /= 4
print("Nilai a /= 4, nilai a menjadi",a)

# Operasi Modulus dan Floor Division
b = 10
print("\nNilai b =",b)
b %= 3
print("Nilai b %= 3, nilai b menjadi",b)

b = 10
print("\nNilai b =",b)
b //= 3
print("Nilai b //= 3, nilai b menjadi",b)

# Pangkat atau Eksponen
b = 10
print("\nNilai b =",b)
b **= 2
print("Nilai b **= 2, nilai b menjadi",b)

# Operasi Logika
# OR
c = True
print("\nNilai c =",c)
c |= False
print("Nilai c |= False, nilai c menjadi",c)
c = False
print("\nNilai c =",c)
c |= False
print("Nilai c |= False, nilai c menjadi",c)

# AND
c = True
print("\nNilai c =",c)
c &= False
print("Nilai c &= False, nilai c menjadi",c)
c = True
print("\nNilai c =",c)
c &= True
print("Nilai c &= True, nilai c menjadi",c)

# XOR
c = True
print("\nNilai c =",c)
c ^= False
print("Nilai c ^= False, nilai c menjadi",c)
c = True
print("\nNilai c =",c)
c ^= True
print("Nilai c ^= True, nilai c menjadi",c)

# Right and Left Shifting
d = 0b0100
print ("\nNilai d =",format(d,"04b"))
d >>= 2
print("Nilai d >>= 2, nilai d menjadi",format(d,"04b"))
d <<= 3
print("Nilai d <<= 3, nilai d menjadi",format(d,"04b"))
