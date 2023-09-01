# Membuat fungsi sederhana
def suaraayam():
    print("Kukuruyuk")

def hargaayam():
    suaraayam()
    print("Harga ayam per 1 kg adalah Rp 20.000,-")

# Membuat fungsi dengan input argument
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargatotal = kg * harga
    print("Harga",kg,"kg ayam adalah",hargatotal)
    
hargaayam()
hargatotalayam(2)
hargatotalayam(5)
hargatotalayam(0.5)
hargatotalayam(1)

print("\n")
# Fungsi dengan argumen sederhana
def siswa(nama):
    print("Nama siswa adalah",nama) 
    
siswa("Mario")

print("\n")
# Fungsi dengan menggunakan keywords arguments
def guru(nama,pelajaran):
    print("Guru ini bernama",nama)
    print("Guru ini mengajar",pelajaran)

guru(nama="Popong",pelajaran="seni rupa")
guru(pelajaran="olahraga",nama="Wawan")
guru("matematika","Raihan") # Ini adalah contoh yang salah

print("\n")
# Fungsi dengan menggunakan default arguments
def penjagasekolah(nama,shift="Siang",galak="Galak"):
    print("Penjaga sekolah ini bernama",nama)
    print("Shiftnya adalah",shift)
    print("Galak atau tidak:",galak)
    
penjagasekolah("Mathias")
penjagasekolah("Maman",shift="Malam")
penjagasekolah("Asep",galak="sangat")
#penjagasekolah(shift="Pagi",galak="sangat") # Contoh yang menghasilkan error
