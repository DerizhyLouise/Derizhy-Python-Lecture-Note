def cek(x):
    y = [0,0]
    for i in range(len(x)):
        z = ord(x[i])
        if z==60:
            y[0] += 1
        elif z==62:
            y[1] += 1
    
    return y

x = input()
y = cek(x)

if y[0] == y[1]:
    print("GOOD")
else:
    print("BAD") 