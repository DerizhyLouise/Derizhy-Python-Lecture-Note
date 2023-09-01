print("Berikut adalah program untuk menentukan palindrom atau bukannya suatu kata")

kata = input("Masukkan sebuah kata: ")

a = ""
b = ""

for i in range (len(kata)):
    a += kata[i]

for i in range (len(kata) -1, -1, -1):
    b += kata[i]
    print(b)
    
if(a==b):
    print("Palindrom")
elif (a!=b):
    print("Bukan Palindrom")