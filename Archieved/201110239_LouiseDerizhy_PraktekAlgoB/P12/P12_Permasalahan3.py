def matrix(baris,kolom,x):
    x = [0]*baris
                
    for i in range (baris):
        x[i] = [0]*kolom

    index = 0
    for i in range (baris):
        for j in range (kolom):
            x[i][j] = z[index]
            index += 1
            
    return x

def transpose(a,b):            
    for i in range (kolom):
        for j in range(baris):
            b[i][j] = a[j][i]
    
    return b            
            
baris, kolom = input().split()
z = [int(i) for i in input().split()]
baris = int(baris)
kolom = int(kolom)

matrix = matrix(baris,kolom,z)
if baris != kolom:
    matrix2 = [[0 for i in range(baris)] for j in range(kolom)]
else:
    matrix2 = [[0 for i in range(kolom)] for j in range(baris)]
hasil = transpose(matrix,matrix2)
        
for i in hasil:
    for j in i:
        print(j,end=" ")
    print()