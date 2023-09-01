class mahasiswa():
    
    def __init__(self, inputnama, inputnim):
        self.nama = inputnama
        self.nim = inputnim
        # __init__ sudah pasti akan dieksekusi
        
    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)
        
    def tidur(self):
        print(self.nama,"tidur di kelas")

'''
Jika tidak memakai __init__ maka untuk merangkai programnya menjadi lebih panjang
Aman = mahasiswa()
Miya = mahasiswa()

Aman.nama = "Amanda"
Miya.nama = "Miya"
'''
Aman = mahasiswa("Amanda", 13317101)
Miya = mahasiswa("Miya", 103117891)

print(Aman.nama)
print(Aman.nim)

Aman.belajar("dengan giat")
Miya.tidur()   