def inputMatrix(baris):
    x = []
    for i in range(baris):
        y = [int (i) for i in input().split()]
        for j in range(len(y)):
            x.append(y[j])
    return x
    
baris = int(input())
kolom = int(input())

x = inputMatrix(baris)
y = inputMatrix(baris)

arr = [0]*baris
index = 0

for i in range(baris):
    arr[i] = [0]*kolom

for i in range(baris):
    for j in range(kolom):
        arr[i][j] = x[index] + y[index]
        index += 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()