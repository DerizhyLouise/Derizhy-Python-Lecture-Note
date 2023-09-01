print("Program Polalop")

x = int(input("Masukkan pola: "))

for i in range(x):
    print(('*'*(i*2+1)).center(x*2+1))
for i in reversed(range(x-1)):
    print(('*'*(i*2+1)).center(x*2+1))