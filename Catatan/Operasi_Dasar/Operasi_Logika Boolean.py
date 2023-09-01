# Operasi Logika Boolean
# Not , Or , And, XOR

# NOT
print("-NOT-")
a = False
c = not a
print("Data a = ",a)
print("Data c = ",c)

# OR
print("\n-OR-")
a = False
b = False
c = a or b
print(a,"or",b,"=",c)
a = False
b = True
c = a or b
print(a,"or",b," =",c)
a = True
b = False
c = a or b
print(a," or",b,"=",c)
a = True
b = True
c = a or b
print(a," or",b," =",c)
# Kesimpulan = Jika salah satu True, maka hasilnya True

# AND
print("\n-AND-")
a = False
b = False
c = a and b
print(a,"and",b,"=",c)
a = False
b = True
c = a and b
print(a,"and",b," =",c)
a = True
b = False
c = a and b
print(a," and",b,"=",c)
a = True
b = True
c = a and b
print(a," and",b," =",c)
# Kesimpulan = Jika salah satu False, maka hasilnya False

# XOR
print("\n-XOR-")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)
a = True
b = True
c = a ^ b
print(a," XOR",b," =",c)
# Kesimpulan = Jika data memiliki perbedaan, maka True