x = [int(i) for i in input().split()]
a = []

for i in range(len(x)):
    if(x[i]==1):
        a.append(i)

for i in reversed(a):
    print(i,end="")