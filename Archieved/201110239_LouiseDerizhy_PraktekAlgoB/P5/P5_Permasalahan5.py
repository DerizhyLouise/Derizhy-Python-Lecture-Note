print("Program penjumlahan biner")

x, y = input().split()
a = 0
b = 0

for i in range(len(x)):
    if(x[i] == "1"):
        a = 2 ** ((len(x) - 1) - i) + a
    elif(x[i] == "0"):
        a = a
print(a)
for j in range(len(y)):
    if(y[j] == "1"):
        b = 2 ** ((len(y) - 1) - j) + b
    elif(y[j] == "0"):
        b = b
print(b)

hasil = a + b
biner = ""

while hasil > 0:
    if (hasil%2 == 0):
        biner = "0" + biner
    else:
        biner = "1" + biner
    hasil //= 2
print(biner,end=" ")