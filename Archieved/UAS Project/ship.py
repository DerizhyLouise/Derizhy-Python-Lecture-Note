## seat Economy
def ship_seat_E():
    rows = ['E']
    arr = []

    for i in range(1, 41):
        if(i <10):
            arr.append(rows[0]+ '0' + str(i))
        else:
            arr.append(rows[0] + str(i))

    return arr

def economy():
    i, j = 0, 0
    print("............ECONOMY CLASS............")
    print()

    while(i < 40):
        while(j < 8):
            if(j == 3):
                print(economy2[i], end = '  ...  ')
                i += 1
                j += 1
            else:
                print(economy2[i], end = ' ')
                i += 1
                j += 1
        j = 0

        print()


## seat Business
def ship_seat_B():
    rows = ['B']
    arr = []

    for i in range(1,21):
        if(i < 10):
            arr.append(rows[0] + '0' +str(i))
        else:
            arr.append(rows[0] + str(i))
    return arr

def business():
    i, j = 0, 0
    print("...........BUSINESS CLASS............")
    print()

    while(i < 20):
        while(j < 5):
            if(j == 2):
                print(business2[i], end = '  ...   ')
                i += 1
                j += 1
            elif(j == 0):
                print('     ' + business2[i], end = ' ')
                i += 1
                j += 1
            else:
                print(business2[i], end = ' ')
                i += 1
                j += 1
        j = 0
        print()
        print()

## seat VIP
def ship_seat_VIP():
    rows = ['VIP']
    arr = []

    for i in range(1, 5):
        arr.append(rows[0] + str(i))

    return arr

def vip():
    i, j = 0, 0
    print("..............VIP CLASS..............")
    print()

    while (i < len(VIP2)):
        while(j < 2):
            if(j == 0):
                print('        ' + VIP2[i], end = '    ...     ')
                j += 1
                i += 1
            else:
                print(VIP2[i], end = ' ')
                j += 1
                i += 1
        print()
        print()
        print()
        j = 0

## Calling Function
economy2 = ship_seat_E()
business2 = ship_seat_B()
VIP2 = ship_seat_VIP()

## ShipList
ShipList = []
for i in range(len(VIP2)):
    ShipList.append(VIP2[i])
for i in range(len(business2)):
    ShipList.append(business2[i])
for i in range(len(economy2)):
    ShipList.append(economy2[i])
    
def checkShip_ID(x):
    check_bool = False
    for i in range(len(ShipList)):
        if ShipList[i] == x:
            return True