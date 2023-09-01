def inputMatrix(baris):
    x = []
    for i in range(baris):
        y = [int (i) for i in input().split()]
        for j in range(len(y)):
            x.append(y[j])
            
    index = 0
    for i in range(baris):
        for j in range(kolom):
            arr[i][j] = x[index]
            index += 1
    return arr

def identitas(x):
    for i in range(baris):
        for j in range(kolom):
            if i == j and x[i][j] != 1:
                return print("O")
            elif i != j and x[i][j] != 0:
                return print("O")
    return print("I")
    
baris, kolom = input().split()
baris = int(baris)
kolom = int(kolom)

arr = [0]*baris
for i in range(baris):
    arr[i] = [0]*kolom

x = inputMatrix(baris)
identitas(x)
