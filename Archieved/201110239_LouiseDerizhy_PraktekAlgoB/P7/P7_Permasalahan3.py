print("Berikut adalah program anagram")

def cekHuruf (kata):
    kata = kata.upper()
    alphabet = [0]*26
    for i in range(len(kata)):
        ascii = ord(kata[i])
        if(ascii>=65 and ascii<=90):
            alphabet[ascii-65] += 1
    return alphabet

def cekAnagram(string1,string2):
    anagram = True
    for i in range(26):
        if(string1[i] != string2[i]):
            anagram = False
            break
    return anagram

x = input()
y = input()
arrX = cekHuruf(x)
arrY = cekHuruf(y)

if(cekAnagram(arrX,arrY)):
    print("anagram")
else:
    print("bukan anagram")