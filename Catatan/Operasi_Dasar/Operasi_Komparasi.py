# Operasi Komparasi
# Setiap hasil operasi komparasi adalah boolean

# < , > , <= , >= , == , != , is , is not

a = 4
b = 2

# Lebih Besar Dari (>)
print("-Lebih Besar Dari-")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Lebih Kecil Dari (<)
print("\n-Lebih Kecil Dari-")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih Besar Sama Dengan (>=)
print("\n-Lebih Besar Sama Dengan-")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Lebih Kecil Sama Dengan (<=)
print("\n-Lebih Kecil Sama Dengan-")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama Dengan (==)
print("\n-Sama Dengan-")
hasil = a == 3
print(a,"==",3,"=",hasil)
hasil = b == 3
print(b,"==",3,"=",hasil)
hasil = b == 2
print(b,"==",2,"=",hasil)

# Tidak Sama Dengan (!=)
print("\n-Tidak Sama Dengan-")
hasil = a != 3
print(a,"!=",3,"=",hasil)
hasil = b != 3
print(b,"!=",3,"=",hasil)
hasil = b != 2
print(b,"!=",2,"=",hasil)

# 'Is' Sebagai komparasi object identity
print("\n-Is-")
x = 5 #Ini adalah assignment membuat object
y = 5
hasil = x is y
print("x is y = ",hasil)

# 'Is Not' Sebagai komparasi object identity
print("\n-Is Not-")
x = 5 #Ini adalah assignment membuat object
y = 5
hasil = x is not y
print("x is not y = ",hasil)