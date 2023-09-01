print("Distinction")

data = []
data = input().split()
data1 = list(dict.fromkeys(data))

for i in range(len(data1)):
    print(data1[i])