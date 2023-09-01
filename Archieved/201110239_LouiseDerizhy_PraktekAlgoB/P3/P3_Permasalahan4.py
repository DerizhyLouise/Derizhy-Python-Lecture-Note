print("Berikut adalah program menentukan gelar dan pujian dalam DOTA")

x = int(input("Jumlah eleminasi sebelumnya: "))
y = int(input("Jumlah eleminasi baru: "))

total = x + y

if(total <= 2):
    gelar1 = "n/a"
elif(total == 3):
    gelar1 = "killing spree"
elif(total == 4):
    gelar1 = "dominating"
elif(total == 5):
    gelar1 = "mega kill"
elif(total == 6):
    gelar1 = "unstopable"
elif(total == 7):
    gelar1 = "wicked sick"
elif(total == 8):
    gelar1 = "monster kill"
elif(total == 9):
    gelar1 = "godlike"
elif(total >= 10):
    gelar1 = "beyond godlike"

if(y<=1):
    gelar2 = "n/a"
elif(y == 2):
    gelar2 = "double kill"
elif(y == 3):
    gelar2 = "triple kill"
elif(y == 4):
    gelar2 = "ultra kill"
elif(y == 5):
    gelar2 = "rampage"

print(x,y,gelar1,gelar2)