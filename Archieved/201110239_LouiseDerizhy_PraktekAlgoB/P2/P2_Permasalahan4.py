fahreinheit = float(input("Masukkan suhu dalam Fahreinheit = ",))
print("Suhu adalah",fahreinheit,"Fahreinheit")

celcius = (5/9) * (fahreinheit - 32)
reamur = (4/9) * (fahreinheit - 32)
kelvin = celcius + 273

print("Suhu dalam Celcius adalah","%.1f"%celcius,"celcius")
print("Suhu dalam Reamur adalah","%.1f"%reamur,"Reamur")
print("Suhu dalam Kelvin adalah","%.1f"%kelvin,"Kelvin")