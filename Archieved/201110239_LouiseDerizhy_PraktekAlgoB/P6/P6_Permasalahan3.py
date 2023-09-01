print("Berikut program koversi, lagi?")

hexa = []
h = input()
for i in range(len(h)):
    hexa += h[i]
hexaValue = ['F','E','D','C','B','A','9','8','7','6','5','4','3','2','1','0']
hexaDeci = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
deci = 0

data1 = len(hexa) - 1

for i in range(len(hexa)):
    for j in range(len(hexaValue)):
        if hexa[i] == hexaValue[j]:
            deci = (16**data1) * hexaDeci[j] + deci
    data1 -= 1

temp = 0 + deci
biner = ""

while temp > 0:
    if(temp%2==0):
        biner = "0" + biner    
    else:
        biner = "1" + biner
    temp //= 2
    
print(deci,biner,sep=" ")