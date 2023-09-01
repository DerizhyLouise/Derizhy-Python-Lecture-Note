def faktorial (n):
    y = 1
    if n > 1:
        return n * faktorial (n-1)
    else:
        return 1
    
x = int(input())
y = int(input())
z = int(input())
print(faktorial(x)/faktorial(y)/faktorial(z))