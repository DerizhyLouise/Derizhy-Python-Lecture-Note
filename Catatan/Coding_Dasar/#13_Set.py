# Set atau Himpunan
# Tuple = ()
# List = []
# Set = {}

superhero = {"Batman","Superman","Ironman","Hawkeye","Captain America"}

superhero.add("Spiderman")
superhero.add("Batman") # Tidak akan menambah karena himpunan

print(superhero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7,11}

print(ganjil.union(genap))
print(ganjil.intersection(prima))

# Hasil print dari set akan acak