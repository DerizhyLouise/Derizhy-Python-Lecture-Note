print("Program pencari huruf awal, tengah, dan akhir")

kata = input("Masukkan sebuah kata dengan banyak huruf ganjil: ")

for i in range (len(kata)):
    if (i == 0):
        print(kata[0])
    elif (i == (len(kata)//2)):
        print(kata[i])
    elif (i == len(kata)-1):
        print(kata[i])