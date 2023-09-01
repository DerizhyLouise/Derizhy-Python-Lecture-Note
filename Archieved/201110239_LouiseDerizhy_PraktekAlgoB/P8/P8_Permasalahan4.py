def cekHuruf (kata):
    kata = kata.lower()
    h1 = 0
    for i in range(len(kata)):
        lol = ord(kata[i])
        if(lol>=94 and lol<=122):
            h1 += ord(kata[i]) - 96
    return h1

def hitung(x):
    h2 = str(x)
    h3 = []
    h4 = 0
    if(x<=9):
        return x
    elif(x>9):
        for i in range(len(h2)):
            h3 += h2[i]
        for i in range(len(h3)):
            h4 += int(h3[i])
        return hitung(h4)

def hitungKecocokan(x,y):
    x1 = cekHuruf(x)
    y1 = cekHuruf(y)
    x2 = hitung(x1)
    y2 = hitung(y1)
    
    if(x2<y2):
        return x2/y2*100
    else:
        return y2/x2*100

a = input("Input First Name \t: ")
b = input("Input Second Name \t: ")

print("Result \t\t\t: %.2f"%hitungKecocokan(a,b),"%")