# Teknik Looping

namaPerusahaanGame = ["Ubisoft",
                      "EA",
                      "Moonton",
                      "Garena",
                      "Gameloft",
                      "Tencent"]

namaGame = ["Growtopia",
            "Battle Field 2",
            "Mobile Legend",
            "Free Fire",
            "NOVA 3",
            "PUBG"]

# enumerate

for index,usaha in enumerate(namaPerusahaanGame):
    print(index,":",usaha)
    
# zip
print("\n")

for usaha,game in zip(namaPerusahaanGame,namaGame):
    print(usaha,"adalah pemilik game",game)

# set
print("\n")

playlist = {"Orange","Lemon","My Love","Pian Pian","Speechless"}
'''
for lagu in playlist:
    print(lagu)
    
Hasilnya akan teracak.
Untuk membuatnya berurutan sesuai abjad masukkan perintah sorted.
'''
for lagu in sorted(playlist):
    print(lagu)

# dictionary
print("\n")

playlist2 = {"Lemon":"Kenshi Yonezhu",
             "My Love":"Lee Hi",
             "Pian Pian":"Dilraba and Silence Wang"}

for i,v in playlist2.items():
    print(i,"oleh",v)

print("\n")

for a in playlist2.keys():
    print(a)
    
print("\n")

for b in playlist2.values():
    print(b)