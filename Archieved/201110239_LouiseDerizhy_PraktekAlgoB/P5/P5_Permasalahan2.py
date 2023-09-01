print("Program pembalik bilangan ganjil dan genap")

x = int(input("Jumlah angka: "))

for i in range(1,x+1):
    if(i % 2 == 1):
        print(i+1)
    else:
        print(i-1)