city = ["Medan","Jakarta","Batam","Surabaya","Badung","Yogyakarta","London","Moskow","Paris","Munich","Berlin","Madrid","New York","Washington DC","Manchester","Dubai","New Delhi","Beijing","Singapore","Hongkong","Rome","Rio de Janeiro","Cape Town","Manila","Kuala Lumpur","Bangkok","Hongkong","Seoul","Tokyo","Monterrey","Cancel Ordering Ticket"]
harbour = ["Hongkong","Medan","Batam","Guangzhou","Busan","Cape Town","Piraeus","Rotterdam","Kopenhagen","Shanghai","Jeddah","Bursaid","Port Royal","Ho Chi Minh","Santos","Valencia","Vanesia","Rio de Janeiro","Sydney","Amsterdam","Lindau","Hamburg","New York","Mumbai","Manila","Tanjung Perak","Nagoya","Khor Fakkan","Cancel Ordering Ticket"]

def receipt(data,price):
    data2 = []
    if data[0] == 0:
        data2.append("Train")
    elif data[0] == 1:
        data2.append("Plane")
    elif data[0] == 2:
        data2.append("Ship")
    
    if data[1] == 0:
        data2.append("Economy")
    elif data[1] == 1:
        data2.append("Business")
    elif data[1] == 2:
        data2.append("VIP")

    if data[0] <= 1 and data[0] >= 0:
        for i in range (len(city)):
            if data[2] == i:
                tempCity = city[i]
                data2.append(tempCity)
    elif data[0] == 2:
        for i in range (len(harbour)):
            if data[2] == i:
                tempHarbour = harbour[i]
                data2.append(tempHarbour)

    if data[5] == 1:
        month = ("January")
    elif data[5] == 2:
        month = ("February")
    elif data[5] == 3:
        month = ("March")
    elif data[5] == 4:
        month = ("April")
    elif data[5] == 5:
        month = ("May")
    elif data[5] == 6:
        month = ("June")
    elif data[5] == 7:
        month = ("July")
    elif data[5] == 8:
        month = ("Auguts")
    elif data[5] == 9:
        month = ("September")
    elif data[5] == 10:
        month = ("October")
    elif data[5] == 11:
        month = ("November")
    elif data[5] == 12:
        month = ("December")
        
    if data[7] == 6:
        data[7] = "06:00"
    elif data[7] == 12:
        data[7] = "12:00"
    elif data[7] == 18:
        data[7] = "18:00"
    
    print("\nTicket Type  \t\t: ", data2[0])
    print("Ticket Class     \t: ", data2[1])
    print("Departure        \t: ", data2[2])
    print("Destination      \t: ", data[3])
    print("Departure Date   \t: ", data[4])
    print("Departure Month  \t: ", month)
    print("Departure Year   \t: ", data[6])
    print("Departure Time   \t:  ", data[7], " WIB",sep="")
    print("Seat ID          \t: ", data[8])
    print("Total Price      \t:  IDR", round(price))