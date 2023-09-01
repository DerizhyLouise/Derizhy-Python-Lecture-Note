print("Berikut adalah program untuk mengkonversi decimal ke biner, octal, dan hexadecimal")

decimal = int(input("Masukkan bilangan decimal: "))

a = ""
b = ""
c = ""
temp3 = decimal
temp2 = decimal
temp1 = decimal

# Decimal -> Biner
biner = temp1
while biner > 0:
    if biner % 2 == 0:
        a = "0" + a
    else:
        a = "1" + a
    biner //= 2
print(a,end=" ")

# Decimal -> Octal
octal = temp2
while octal > 0:
    if octal % 8 == 0:
        b = "0" + b
    elif octal % 8 == 1:
        b = "1" + b
    elif octal % 8 == 2:
        b = "2" + b
    elif octal % 8 == 3:
        b = "3" + b
    elif octal % 8 == 4:
        b = "4" + b
    elif octal % 8 == 5:
        b = "5" + b
    elif octal % 8 == 6:
        b = "6" + b
    else:
        b = "7" + b
    octal //= 8
print(b,end=" ")

# Decimal -> Hexadecimal
hexa = temp3
while hexa > 0:
    if hexa % 16 == 0:
        c = "0" + c
    elif hexa % 16 == 1:
        c = "1" + c
    elif hexa % 16 == 2:
        c = "2" + c
    elif hexa % 16 == 3:
        c = "3" + c
    elif hexa % 16 == 4:
        c = "4" + c
    elif hexa % 16 == 5:
        c = "5" + c
    elif hexa % 16 == 6:
        c = "6" + c
    elif hexa % 16 == 7:
        c = "7" + c
    elif hexa % 16 == 8:
        c = "8" + c
    elif hexa % 16 == 9:
        c = "9" + c
    elif hexa % 16 == 10:
        c = "A" + c
    elif hexa % 16 == 11:
        c = "B" + c
    elif hexa % 16 == 12:
        c = "C" + c
    elif hexa % 16 == 13:
        c = "D" + c
    elif hexa % 16 == 14:
        c = "E" + c
    else:
        c = "F" + c
    hexa //= 16
print(c)