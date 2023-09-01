print("Berikut adalah program diaas rerata!")

def diatasRerata(arr):
    total = 0
    
    for i in range(len(arr)):
        total += arr[i]
        
    rata = total / len(arr)
    hasil = 0
    
    for i in range(len(arr)):
        if(arr[i] > rata):
            hasil += 1

    hasilAkhir = hasil / len(arr) * 100
    return hasilAkhir

arr = []
x = list(map(int,input().split()))
print("%.3f"%diatasRerata(x),"\b%")