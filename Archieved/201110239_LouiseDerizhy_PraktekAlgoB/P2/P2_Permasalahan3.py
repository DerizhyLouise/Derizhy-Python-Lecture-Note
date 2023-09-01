jarak = int(input("Masukkan jarak perjalanan semut: "))

km = jarak // 100000
jarak = jarak % 100000
m = jarak // 100
jarak = jarak % 100
cm = jarak

print(km,"km,",m,"m,",cm,"cm")