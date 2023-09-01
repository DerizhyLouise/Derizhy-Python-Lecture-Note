baris, kolom = input().split()
x = [int (i) for i in input().split()]

baris = int(baris)
kolom = int(kolom)
arr = [0]*baris

for i in range(baris):
    arr[i] = [0]*kolom

index = 0
for i in range(baris):
    for j in range(kolom):
        arr[i][j] = x[index]
        index += 1
            
print(arr)
for i in arr:
    for j in i:
        print(j,end=" ")
    print()    