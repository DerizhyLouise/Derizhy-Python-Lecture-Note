print("Berikut adalah program untuk mendeteksi apakah segitiga siku-siku atau bukan")

a = int(input("Masukkan sisi a: "))
b = int(input("Masukkan sisi b: "))
c = int(input("Masukkan sisi c: "))

y = "segitiga siku-siku"
n = "bukan segitiga siku-siku"


if(a <= b <= c):
    a1 = a
    b1 = b
    c1 = c
elif(a <= c <= b):
    a1 = a
    b1 = c
    c1 = b
elif(b <= c <= a):
    a1 = b
    b1 = c
    c1 = a
elif(b <= a <= c):
    a1 = b
    b1 = a
    c1 = c
elif(c <= a <= b):
    a1 = c
    b1 = a
    c1 = b
elif(c <= b <= a):
    a1 = c
    b1 = b
    c1 = a

a2 = a1 ** 2
b2 = b1 ** 2
c2 = c1 ** 2

ab = a2 + b2
    
if(c2 == ab):
    print(a1,b1,c1,y)
else:
    print(a1,b1,c1,n)