n = int(input())
y = 1
x = list(map(int,input().split()))
for i in range(len(x)):
    y = y * (x[i]*x[i])

print(y)