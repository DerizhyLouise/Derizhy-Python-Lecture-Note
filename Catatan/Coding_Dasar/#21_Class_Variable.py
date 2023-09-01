class mahasiswa():
    
    jumlahmahasiswa = 0
    
    def __init__(self, inputnama, inputnim):
        self.nama = inputnama # Public
        self.nim = inputnim # Public
        mahasiswa.jumlahmahasiswa += 1
        
aman = mahasiswa("Amanda", 1111111)
miya = mahasiswa("Miya", 2222222)
budi = mahasiswa("Budiono", 3333333)

print(mahasiswa.jumlahmahasiswa)