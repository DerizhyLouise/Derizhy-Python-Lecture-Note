# if

nilai1 = 75
nilai2 = 80

if nilai1 == 75:
    print("Step 1") # Perintah wajib di tab
    print("Nilai anda =", nilai1)
    if nilai2 == 80:    # Ini adalah Nesting    
        print("Step 2")
        print("Nilai anda =", nilai2)

# elif
# else

nilai = float(input("\nMasukkan nilai anda : ",))

if 90 <= nilai <= 100:
    print("Nilai anda adalah A")
elif 80 <= nilai < 90:
    print("Nilai anda adalah B")
elif 70 <= nilai < 80:
    print("Nilai anda adalah C")
elif 60 <= nilai < 70:
    print("Nilai anda adalah D")
elif 50 <= nilai < 60:
    print("Nilai anda adalah E")
else:
    print("Nilai anda adalah F")