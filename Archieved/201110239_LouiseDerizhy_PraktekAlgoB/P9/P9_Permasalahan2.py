def change(var1):
    waw = []
    for i in range(len(var1)):
        waw.append(int(var1[i]))
    return waw

def cek1(a,b,c):
    result = True
    if(c=="samping"):
        for i in range(len(a)):
            if(a[i]==b):
                result = False
                break
    return result

def cek2(a,b):
    result = True
    for i in range(len(a)):
        if(a[i]==b):
            result = False
            break
    return result
    
def perubahan(arr,perintah,tambah,cek):
    if(cek):
        if(perintah=="awal"):
            arr.insert(0,tambah)
            print(arr)
        elif(perintah=="akhir"):
            arr.append(tambah)
            print(arr)
    else:
        print(arr)
        
def perubahanKhusus(arr,tambah,cek1,cek2):
    if(cek2):
        if(cek1):
            print(arr)
        else:
            for i in range(len(arr)):
                if(arr[i]==e):
                    ke = i + 1
                    break
            arr.insert(ke,tambah)
            print(arr)
    else:
        print(arr)
    
a = input().split()
b = input().split()
c = b[0]
d = int(b[1])
a = change(a)
if(len(b)==3):
    e = int(b[2])
    cek1 = cek1(a,e,c)
    cek2 = cek2(a,d)
    perubahanKhusus(a,d,cek1,cek2)
else:
    cek = cek2(a,d)
    perubahan(a,c,d,cek)