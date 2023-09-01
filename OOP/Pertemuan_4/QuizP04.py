# Tugas Pemrograman Berorientasi Objek
# Nama              : Louise Derizhy
# Kelas             : IF-B Sore
# Dosen Pengampu    : Khristian Tanselmus, S.Kom., M.TI.

class televisi:
    __channels = ["GTV", "ANTV", "SCTV", "TransTV", "Trans7", "Indosiar", "NetTV", "TVOne", "MetroTV", "RCTI", "MNCTV"]
    __deskripsi = ""
    __volume = 0
    __channelAktif = 1
    __jumlahChannel = len(__channels)
    
    def __init__(self, deskripsi, jumlahChannel):
        self.deskripsi = deskripsi
        self.jumlahChannel = jumlahChannel

    def getDeskripsi (self):
        print(f"Deskripsi : {self.deskripsi}\n")
    
    def getJumlahChannel (self):
        print(f"Jumlah Channel : {self.__jumlahChannel}\n")
    
    def getJumlahChannelTerdaftar (self):
        print(f"Jumlah Channel Terdaftar: {self.jumlahChannel}\n")
    
    def getChannels (self):
        index = 1
        print("Daftar Channel")
        for i in self.__channels:
            print(index, ". ", i, sep="")
            index += 1
        print("\n")
    
    def setChannels (self, set):
        self.__channels.extend(set)
        self.__jumlahChannel = len(self.__channels)
        print("Channel telah dimasukkan")
        self.getJumlahChannel()
        self.getChannels()
    
    def getChannelAktif (self):
        print(f"Channel yang aktif : {self.__channels[self.__channelAktif-1]}\n")
    
    def setChannelAktif (self, set):
        print(f"Channel di set ke {set}")
        self.__channelAktif = set
        self.getChannelAktif()
    
    def getVolume (self):
        print(f"Volume saat ini : {self.__volume}\n")
    
    def setVolume (self, set):
        self.__volume = set
        print(f"Volume di set ke : {self.__volume}\n")
        
    def bukaTelevisi(self):
        print('''
Remot TV
Menu :
0. Deskripsi TV
1. Jumlah Channel
2. Jumlah Channel Terdaftar
3. Channel yang Terekam di TV
4. Menset Channel ke dalam TV
5. Mengambil Channel yang Aktif
6. Menset Channel yang Aktif
7. Mengambil Volume TV
8. Menset Volume TV
9. Tutup Televisi
                ''')
        while True:
            while True:
                try:
                    menu = int(input("Silahkan input menu yang ingin diakses : "))
                    if (menu < 0) or (menu > 9): raise ValueError
                    break
                except ValueError: print("Menu tidak valid. Pilih menu antara 0-9!")
                    
            if menu == 0: self.getDeskripsi()
            elif menu == 1: self.getJumlahChannel()
            elif menu == 2: self.getJumlahChannelTerdaftar()
            elif menu == 3: self.getChannels()
            elif menu == 4:
                temp = input("Masukkan Channel yang akan Dimasukkan :").split()
                self.setChannels(temp)
            elif menu == 5: self.getChannelAktif()
            elif menu == 6:
                while True:
                    try:
                        temp = int(input("Masukkan Channel yang Diinginkan : "))
                        if (temp < 0) or (temp > self.__jumlahChannel): raise ValueError
                        else: break
                    except ValueError: print(f"Channel tidak ditemukan (Masukkann angka)")
                        
                self.setChannelAktif(temp)
            elif menu == 7: self.getVolume()
            elif menu == 8:
                while True:
                    try:
                        temp = int(input("Masukkan Volume TV yang Diinginkan : "))
                        if (temp < 0) or (temp > 100): raise ValueError
                        else: break
                    except ValueError: print("Volume hanya dapat diakses dari 0-100")
                self.setVolume(temp)
            elif menu == 9:
                print("Televisi telah ditutup")
                break
            print("="*50)

class televisiModern(televisi):
    __modusTampilan = 0
    __halamanTeletext = 1
    __discTray = "Blablabla"
    tv = 0
    teletext = 1
    
    def __init__(self, deskripsi, jumlahChannel, modusTampilan):
        super().__init__(deskripsi, jumlahChannel)
        self.modusTampilan = modusTampilan
        
    def setHalamanTeletext (self, set):
        self.__halamanTeletext = set
        print(f"Halaman Teletext telah diset ke {self.__halamanTeletext}\n")
    
    def setModusTampilan (self):
        self.__modusTampilan = self.modusTampilan
        print(f"Modul Tampilan telah diset ke {self.__modusTampilan}\n")
    
    def getModusTampilan (self):
        print(f"Modul Tampilan saat ini : {self.__modusTampilan}\n")
    
    def getDiscTray (self):
        print(f"Isi dari Disc Tray : {self.__discTray}\n")
    
    def setDiscTray (self, set):
        self.__discTray = set
        print(f"Isi dari Disc Tray telah diubah menjadi : {self.__discTray}\n")
    
    def PlayCD (self):
        print(f"Sedang Memutar isi dari Disc Tray : {self.__discTray}\n")
        
    def getHalamanTeletext (self):
        print(f"Membuka halaman {self.__halamanTeletext}\n")
    
    def bukaTelevisi (self):
        print('''
Remot TV
Menu :
 0. Deskripsi TV
 1. Jumlah Channel
 2. Jumlah Channel Terdaftar
 3. Channel yang Terekam di TV
 4. Menset Channel ke dalam TV
 5. Mengambil Channel yang Aktif
 6. Menset Channel yang Aktif
 7. Mengambil Volume TV
 8. Menset Volume TV
 9. Menset Halaman Teletext
10. Menset Modus Tampilan
11. Mengambil Modus Tampilan
12. Mengambil Disc Tray
13. Menset Disc Tray
14. Memutar CD
15. Mengambil Halaman Teletext
16. Tutup Televisi
                ''')
        while True:
            while True:
                try:
                    menu = int(input("Silahkan input menu yang ingin diakses : "))
                    if (menu < 0) or (menu > 16): raise ValueError
                    break
                except ValueError: print("Menu tidak valid. Pilih menu antara 0-9!")
                    
            if menu == 0: self.getDeskripsi()
            elif menu == 1: self.getJumlahChannel()
            elif menu == 2: self.getJumlahChannelTerdaftar()
            elif menu == 3: self.getChannels()
            elif menu == 4:
                temp = input("Masukkan Channel yang akan Dimasukkan :").split()
                self.setChannels(temp)
            elif menu == 5: self.getChannelAktif()
            elif menu == 6:
                while True:
                    try:
                        temp = int(input("Masukkan Channel yang Diinginkan : "))
                        if (temp < 0) or (temp > self.__jumlahChannel): raise ValueError
                        else: break
                    except ValueError: print(f"Channel tidak ditemukan (Masukkann angka)")
                self.setChannelAktif(temp)
            elif menu == 7: self.getVolume()
            elif menu == 8:
                while True:
                    try:
                        temp = int(input("Masukkan Volume TV yang Diinginkan : "))
                        if (temp < 0) or (temp > 100): raise ValueError
                        else: break
                    except ValueError: print("Volume hanya dapat diakses dari 0-100")
                self.setVolume(temp)
            elif menu == 9: 
                while True:
                    try:
                        temp = int(input("Masukkan Halaman Teletext : "))
                        break
                    except: print("Input tidak valid. Masukkan angka!")
                self.setHalamanTeletext(temp)
            elif menu == 10: self.setModusTampilan()
            elif menu == 11: self.getModusTampilan()
            elif menu == 12: self.getDiscTray()
            elif menu == 13: 
                temp = input("Masukkan setting Disc Tray: ")
                self.setDiscTray(temp)
            elif menu == 14: self.PlayCD()
            elif menu == 15: self.getHalamanTeletext()
            elif menu == 16:
                print("Televisi telah ditutup")
                break
            print("="*50)
        
a = televisi ("Ini adalah Televisi A", 9)
b = televisi ("Ini adalah Televisi B", 10)
c = televisiModern ("Ini adalah Televisi Modern C", 8, 1)
d = televisiModern ("Ini adalah Televisi Modern D", 6, 2)

# Silahkan hapus tanda (#) untuk menyalakan televisi
#a.bukaTelevisi()
#b.bukaTelevisi()
#c.bukaTelevisi()
d.bukaTelevisi()

#Catatan : Maaf pak, untuk bagian televisi modern atribut dan metodenya
#saya kurang paham mengenai apa itu teletext, modus tampilan, disctray, dll
        
        
        