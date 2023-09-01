# Operasi Bitwise dan Operasi Biner

a = 9
b = 5

# Bitwise Or (|)
c = a | b
print("-OR-")
print("Nilai :",a," , binary :",format(a,"08b"))
print("Nilai :",b," , binary :",format(b,"08b"))
print("-------------------------------(|)")
print("Nilai :",c," , binary :",format(c,"08b"))

# Bitwise And (&)
c = a & b
print("-AND-")
print("Nilai :",a," , binary :",format(a,"08b"))
print("Nilai :",b," , binary :",format(b,"08b"))
print("-------------------------------(&)")
print("Nilai :",c," , binary :",format(c,"08b"))

# Bitwise XOR (^)
c = a ^ b
print("-XOR-")
print("Nilai :",a," , binary :",format(a,"08b"))
print("Nilai :",b," , binary :",format(b,"08b"))
print("-------------------------------(^)")
print("Nilai :",c," , binary :",format(c,"08b"))

# Bitwise NOT (~)
c = ~a
print("Nilai :",a," , binary :",format(a,"08b"))
print("-------------------------------(~)")
print("Nilai :",c," , binary :",format(c,"08b"))

# Right Shifting (>>)
c = a >> 2
print("Nilai :",a," , binary :",format(a,"08b"))
print("-------------------------------(>>)")
print("Nilai :",c," , binary :",format(c,"08b"))

# Left Shifting (<<)
c = a << 3
print("Nilai :",a," , binary :",format(a,"08b"))
print("-------------------------------(>>)")
print("Nilai :",c," , binary :",format(c,"08b"))
