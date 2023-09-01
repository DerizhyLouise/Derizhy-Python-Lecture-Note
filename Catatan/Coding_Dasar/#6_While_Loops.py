angka = 0

while angka < 5:
    print("Nilai angka adalah :",angka)
    angka += 1
    # Hati-hati terhadapat while
print ("Di luar while")

start = True
angka = 0

while start:
    print("Di dalam while")
    if angka is 100:
        start = False
        print("Angka 100 sudah ditemukan")
    angka += 1
    
# Else
print("\n")

angka = 0

while angka < 5:
    print("Nilai angka adalah :",angka)
    angka += 1
else:
    print("Nilai angka di akhir while adalah",angka)
print ("Di luar while")

# Break
print("\n")
angka = 0
while angka < 10:
    if angka is 5:
        print("Checkpoint 1")
        break # Langsung ke luar dari while
        print("Checkpoint 2")
    print("Nilai angka adalah :",angka)
    angka += 1
else:
    print("Nilai angka di akhir while adalah",angka)

print("Di luar while")

# Continue
print("\n")
angka = 0
while angka < 10:
    if angka is 5:
        print("Checkpoint 1")
        angka += 1
        continue # akan terus melanjutkan perintah di atas hingga menyelesaikan while
        print("Checkpoint 2")
    print("Nilai angka adalah :",angka)
    angka += 1
else:
    print("Nilai angka di akhir while adalah",angka)

print("Di luar while")