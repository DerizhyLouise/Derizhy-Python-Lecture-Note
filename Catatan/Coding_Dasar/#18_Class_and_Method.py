# Class
class mahasiswa():
    nama = "nama"
    
    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)
        
    def tidur(self):
        print(self.nama,"tidur di kelas")

# Main Program
Aman = mahasiswa()
Miya = mahasiswa()

Aman.nama = "Amanda"
Miya.nama = "Miya"

Aman.belajar("dengan giat")
Miya.tidur()