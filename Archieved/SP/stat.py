import math

x = [float(i) for i in input().split()]

for i in range(len(x)-1):
    for j in range(i + 1, len(x)):
        if x[i] >= x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp

print("\n-------------------------------------------------------------")
print("\nSort : \n")
for i in range(len(x)):
    print(x[i], end=" ")
    
total = 0
var = 0
varS = 0
count = len(x)
for i in range(len(x)):
    total += x[i]
    
mean = total/len(x)
Range = x[-1] - x[0]

for i in range(len(x)):
    var += (x[i] - mean) ** 2
    varS += (x[i] - mean) ** 2
var *= 1/(len(x)-1) 
varS *= 1/(len(x)) 

sP = math.sqrt(var)
sS = math.sqrt(varS)
    
print("\n-------------------------------------------------------------")
print("\nCount                         = ", count)
print("\nSum                           = ", total)
print("\nMean                          = ", mean)
print("\nVariance Population           = ", var)
print("\nVariance Sample               = ", varS)
print("\nRange                         = ", Range)
print("\nStandard Deviation Population = ", sP)
print("\nStandard Deviation Sample     = ", sS)
