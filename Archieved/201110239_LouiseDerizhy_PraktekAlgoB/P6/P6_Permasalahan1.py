print("Program Hitung Hitung Hitung 1")

kata = input().lower()
vokal = ["a","e","i","o","u"]
data = [0,0,0,0,0]

for i in range(len(kata)):
    for k in range(len(vokal)):
        if kata[i] == vokal[k]:
            data[k] += 1
        
for j in range(len(data)):
    print(data[j])