from random import randint

n = int(input())

for i in range(n):
    dadu1 = randint(1,6)
    print(dadu1)
    for i in range(n):
        dadu2 = randint(1,6)
        print(dadu2)
        break
    
if dadu1 == dadu2:
    print("Yes")
else:
    print("No")