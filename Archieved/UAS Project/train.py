## Seat name gen(A and C)
def train_seat():
    rows = ['A', 'C']
    arr = []

    for i in range(12):
        arr.append([])

        for j in range(2):
            arr[i].append(str(i+1)+rows[j])
            
    return arr

## Seat name gen(B and D)
def train_seat2():
    rows = ['B', 'D']
    arr = []

    for i in range(12):
        arr.append([])

        for j in range(2):
            arr[i].append(str(i+1)+rows[j])


    return arr

## Calling Function
seat1 = train_seat()
seat2 = train_seat2()


## TrainList
TrainList = []

for i in range(len(seat1)):
    for j in range(len(seat1[i])):
        if(i < 9):
            TrainList.append('0' + seat1[i][j])
            TrainList.append('0' + seat2[i][j])
        else:
            TrainList.append(seat1[i][j])
            TrainList.append(seat2[i][j])

## Loop to make pattern of seats arrangement

def train():
    print()

    for i in range(9):
        for j in range(2):
            print('0'+seat1[i][j], end = ' ')
            print('0'+seat2[i][j], end = ' ')
            
            if(j == 0):
                print("  -  ", end = ' ')

        print()

    for i in range(9, 12):
        for j in range(2):
            print(seat1[i][j], end = ' ')
            print(seat2[i][j], end = ' ')

            if(j == 0):
                print("  -  ", end = ' ')

        print()

def checkTrain_ID(x):
    check_bool = False
    for i in range(len(TrainList)):
        if TrainList[i] == x:
            return True