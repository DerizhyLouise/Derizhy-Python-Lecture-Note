print("Berikut adalah program untuk menghitung luas dan volume bola")
import decimal

r = float(input("Masukkan nilai jari-jari: "))
phi = 22 / 7
luas = 4 * phi * r * r
volume = (4 / 3) * phi * (r**3)

print("Hasil dari luas bola tersebut adalah","%.3f" % luas)
print("Hasil dari volume bola tersebut adalah","%.3f" % volume)

print("Dengan round",round(luas,3))