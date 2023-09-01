class mahasiswa():
    
    jurusan = "Teknik Informatika"
    __nilai = 0 # Private
    
    def __init__(self, inputnama, inputnim):
        self.nama = inputnama # Public
        self.nim = inputnim # Public
        
    def uts (self, inputnilai):
        self.__nilai += inputnilai
        
    def uas(self, inputnilai):
        self.__nilai += inputnilai
    
    def check(self):
        if self.__nilai <= 50:
            print(self.nama,"tidak lulus")
        else:
            print(self.nama,"lulus")
            
aman = mahasiswa("Amanda", 111111111)
miya = mahasiswa("Miya",22222222)

aman.uts(10)
aman.uas(50)
aman.check()

miya.uts(30)
miya.uas(15)
miya.check()