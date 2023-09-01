def cek(a,x):
    if a:
        print(x[0],len(x)-2,x[-1],sep="")
    else:
        print(x)

x = input()

if len(x) >= 10:
    a = True
else:
    a = False

cek(a,x)