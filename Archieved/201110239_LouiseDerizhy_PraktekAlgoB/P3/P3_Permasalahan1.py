print("Berikut adalah program untuk mencari posisi\n")

x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
kuadran = input("Tentukan posisi kuadran (Input dengan I, II, III, atau IV): ")

if(kuadran == "I"):
    print("(",x,",",y,")",sep="")
elif(kuadran == "II"):
    print("(-",x,",",y,")",sep="")
elif(kuadran == "III"):
    print("(-",x,",-",y,")",sep="")
elif(kuadran == "IV"):
    print("(",x,",-",y,")",sep="")
else:
    print("Warning! Input dengan I, II, III, atau IV!")