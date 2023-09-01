# Seat name gen(A and D)
def ap_seat():
    rows = ['A', 'G']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(G and K)
def ap_seat2():
    rows = ['D', 'K']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(A and F)
def ap_seat3():
    rows = ['A', 'F']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(C AND G)
def ap_seat4():
    rows = ['C', 'G']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(D AND H)
def ap_seat5():
    rows = ['D', 'H']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(E and K)
def ap_seat6():
    rows = ['E', 'k']
    arr = []

    for x in range(30):
        arr.append([])

        for y in range(2):
            arr[x].append(str(x+1)+rows[y])

    return arr


# Seat name gen(A and F)
def ap_seat7():
    rows = ['A', 'F']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(C AND G)
def ap_seat8():
    rows = ['C', 'G']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(D AND H)
def ap_seat9():
    rows = ['D', 'H']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(2):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Seat name gen(K)
def ap_seat10():
    rows = ['K']
    arr = []
    for x in range(30):
        arr.append([])
        for y in range(1):
            arr[x].append(str(x+1)+rows[y])
    return arr


# Calling Function
seat1 = ap_seat()
seat2 = ap_seat2()
seat3 = ap_seat3()
seat4 = ap_seat4()
seat5 = ap_seat5()
seat6 = ap_seat6()
seat7 = ap_seat7()
seat8 = ap_seat8()
seat9 = ap_seat9()
seat10 = ap_seat10()


# airplane list
airplane_list = []
for x in range(len(seat1)):
    for y in range(len(seat1[x])):
        if x < 2:
            airplane_list.append(seat1[x][y])
            airplane_list.append(seat2[x][y])
        elif x >= 4 and x <= 17:
            airplane_list.append(seat3[x][y])
            airplane_list.append(seat4[x][y])
            airplane_list.append(seat5[x][y])
            airplane_list.append(seat6[x][y])
        elif x >= 19 and x <= 29:
            airplane_list.append(seat7[x][y])
            airplane_list.append(seat8[x][y])
            airplane_list.append(seat9[x][y])
for x in range(len(seat10)):
    for y in range(len(seat10[x])):
        if x >= 19 and x <= 29:
            airplane_list.append(seat10[x][y])


# Loop to make pattern of seats arrangement
def vip_class():
    print("VIP Class")
    for x in range(2):
        for y in range(2):
            print('', end=' ')
            print(seat1[x][y], end='     ')
            print("-", end='     ')
            print(seat2[x][y], end='   ')
            if(y == 0):
                print("", end='')
        print()


def business_class():
    print("Business Class")
    for x in range(4, 9):
        for y in range(2):
            print(' ' + seat3[x][y], end='  ')
            print(seat4[x][y], end=' ')
            print("-", end='  ')
            print(seat5[x][y], end='  ')
            print(seat6[x][y], end=' ')
            if(y == 0):
                print("", end='')
        print()

    for x in range(9, 18):
        for y in range(2):
            print(seat3[x][y], end=' ')
            print(seat4[x][y], end=' ')
            print("-", end=' ')
            print(seat5[x][y], end=' ')
            print(seat6[x][y], end=' ')
            if(y == 0):
                print("", end='')
        print()


def economy_class():
    print("Economy Class")
    for x in range(19, 30):
        for y in range(2):
            print(seat7[x][y], end=' ')
            print(seat8[x][y], end='  ')
            print("-", end='  ')
            print(seat9[x][y], end=' ')
        for z in range(1):
            print(seat10[x][z], end=' ')
            if(z == 0):
                print("", end='')
        print()
        
def checkPlane_ID(x):
    check_bool = False
    for i in range(len(airplane_list)):
        if airplane_list[i] == x:
            return True