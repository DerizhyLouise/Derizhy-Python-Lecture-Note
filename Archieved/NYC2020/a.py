x = int(input())
a = str(x)
b = []
c = [0,0]
b3 = []

for i in range(len(a)):
    b += a[i]
b1 = b[0]+b[1]
b2 = b[2]+b[3]
b3.append(b1)
b3.append(b2)

for i in range(len(b3)):
    c[i] += int(b3[i])

if(c[0]<=12 and c[0]>=1):
    if(c[1]<=12 and c[1]>=1):
        print("AMBIGU")
    elif(c[1]>=1 and c[1]<=99):
        print("MMYY")
    else:
        print("TIDAK JELAS")
elif(c[1]<=99 and c[1]>=1):
    if(c[0]<=12 and c[0]>=1):
        print("AMBIGU")
    elif(c[0]>=1 and c[0]<=99):
        print("YYMM")
    else:
        print("TIDAK JELAS")
    