from abc import ABC, abstractmethod

def cekNama(nama):
    for kar in nama:
        if(not(ord("A") <=  ord(kar) <= ord("Z") or ord("a") <=  ord(kar) <= ord("z") or kar == " ")):
            return False
    return True

class absHasil(ABC):
    @abstractmethod
    def hasil():
        pass
    
class simpanData(absHasil):
    def hasil(nama):
        if (cekNama(nama)):
            print(f"{nama} berhasil disimpan ke dalam data")
        else:
            print("Mohon maaf nama tidak dapat disimpan")
            
class loginNama(absHasil):
    def hasil(nama):
        if (cekNama(nama)):
            print(f"{nama} sesuai ketentuan dan anda bisa login")
        else:
            print("Mohon maaf nama tidak sesuai dan tidak dapat login")
            
if __name__ == '__main__':
    nama = "Blablabal adaw"
    for i in absHasil.__subclasses__():
        i.hasil(nama)