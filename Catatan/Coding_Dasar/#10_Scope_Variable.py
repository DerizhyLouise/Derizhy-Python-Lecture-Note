# Scope Variable Local
namaKucing = "Cassandra"

def ubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print("Saya ubah nama kucing menjadi",namaBaru)
    
ubahNamaKucing("Kettie")
print("Nama kucing saya menjadi",namaKucing)    

print("\n")
# Scope Variable Local
namaKucing = "Cassandra"
namaMakanan = "Royal Canin"
def ubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print("Saya ubah nama kucing menjadi",namaBaru)
    
def kasihMakanKucing (makanan,nama):
    global namaKucing,namaMakanan
    namaKucing = nama
    namaMakanan = makanan
    
ubahNamaKucing("Kettie")
kasihMakanKucing("Universal","Alex")
print("Nama kucing saya menjadi",namaKucing,"dan makan",namaMakanan)