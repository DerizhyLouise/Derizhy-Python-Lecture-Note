# Fungsi dalam Return Value
def kuadrat(argumen):
    total = argumen**2
    print("Nilai kuadrat dari",argumen,"adalah",total)
    return total

a = kuadrat(4)
print(a)

print("\n")
# Fungsi dengan Return Value dan Multiple Argument
def tambah(argumen1,argumen2):
    total = argumen1+argumen2
    print(argumen1,"+",argumen2,"=",total)
    return total

def kali(argumen1,argumen2):
    total = argumen1*argumen2
    print(argumen1,"*",argumen2,"=",total)
    return total

a = tambah(5,7)
b = tambah(4,3)
print(a)
print("\n")

c = kali(a,b)
print(c)
print("\n")

d = kali(7,tambah(4,6)) # tambah(4,6) akan dieksekusi terlebih dahulu
print(d)