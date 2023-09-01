print("Program Hitung Hitung Hitung 2")

kata = input().lower()
data = [0,0]

for j in range(len(kata)):
    if(kata[j] == "a"):
        data[0] += 1
    elif(kata[j] == "e"):
        data[0] += 1
    elif(kata[j] == "i"):
        data[0] += 1
    elif(kata[j] == "o"):
        data[0] += 1
    elif(kata[j] == "u"):
        data[0] += 1
    else:
        data[1] += 1

for k in range(len(data)):
    print(data[k])