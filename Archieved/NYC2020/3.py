import math
#n = int(input())
#x = [int(n) for n in input().split()]

a = []
b = 1
for i in range(100):
    a += pow(10,b)[i]
    b +=1

print(a)