import time_validity as val
import train
import plane
import ship

# Data Storing
data = []
city = ["Medan","Jakarta","Batam","Surabaya","Badung","Yogyakarta","London","Moskow","Paris","Munich","Berlin","Madrid","New York","Washington DC","Manchester","Dubai","New Delhi","Beijing","Singapore","Hongkong","Rome","Rio de Janeiro","Cape Town","Manila","Kuala Lumpur","Bangkok","Hongkong","Seoul","Tokyo","Monterrey","Cancel Ordering Ticket"]
harbour = ["Hongkong","Medan","Batam","Guangzhou","Busan","Cape Town","Piraeus","Rotterdam","Kopenhagen","Shanghai","Jeddah","Bursaid","Port Royal","Ho Chi Minh","Santos","Valencia","Vanesia","Rio de Janeiro","Sydney","Amsterdam","Lindau","Hamburg","New York","Mumbai","Manila","Tanjung Perak","Nagoya","Khor Fakkan","Cancel Ordering Ticket"]

def opening():
    print("Welcome to our Online Ticket Mart!\n")
    print("We have newest transportation technology that")
    print("can take you to your destination very fast")
    print("Even our train may cross the sea ^^\n")
    
def asking():
    input1_bool = True
    ticketType_bool = False
    
    while input1_bool:
        input1 = input("Do you want to order ticket? (Y/N) ")
    
        if input1 == "Y":
            input1_bool = False
            ticketType_bool = True
        elif input1 == "N":
            input1_bool = False
            return print("\nGood bye!")
        else:
            print("Invalid input, only accept Y and N answer.")
            input1_bool = True
    
    return ticketType_bool

def ticketType(ticketType_bool):
    inputTicketType_bool = True
    quitBool = False
    ticketClass_bool = False
    ticketType = ["Train \t: IDR 100,000","Plane \t: IDR 500,000","Ship \t: IDR 250,000","Cancel Ordering Ticket"]
    ticketType2 = ["Train","Plane","Ship"]
    type_index = 0

    if ticketType_bool:
        print("\nWhich ticket do you want to order?")
    
        for i in ticketType:
            print(str(type_index) + ". " + i)
            type_index += 1
        
        while inputTicketType_bool:   
            inputTicketType = int(input("Input number only : "))
            if inputTicketType >= 0 and inputTicketType <= 3:
                inputTicketType_bool = False
            
                if inputTicketType == 3:
                    quitBool = True
            else:
                print("Invalid input")
    
        if quitBool:
            return print("\nGood bye!")
        else:
            print("You choose", ticketType2[inputTicketType], "ticket")
            ticketClass_bool = True
        
        data.append(inputTicketType)
    
    return(ticketClass_bool)

def ticketClass(ticketClass_bool):
    inputTicketClass_bool = True
    departure_bool = False
    quitBool = False
    seatClass = ["Economic \t: No additional price","Business \t: 10% additional price","VIP \t: 50% additional price","Cancel Ordering Ticket"]
    seatClass2 = ["Economic","Business","VIP"]
    class_index = 0

    if ticketClass_bool:
        print("\nChoose your seat class")
    
        for i in seatClass:
            print(class_index, ". ", i)
            class_index += 1
    
        while inputTicketClass_bool:
            inputTicketClass = int(input("Input number only : "))
            if inputTicketClass <= 3 and inputTicketClass >= 0:
                inputTicketClass_bool = False
            
                if inputTicketClass == 3:
                    quitBool = True
            else:
                print("Invalid input")
        
        if quitBool:
            return print("\nGood bye!")
        else:
            print("You choose", seatClass2[inputTicketClass], "class")
            departure_bool = True
            
        data.append(inputTicketClass)
        
    return departure_bool

def departure(departure_bool,data):
    inputDeparture_bool = True
    destination_bool = False
    quitBool = False
    departure_index = 0

    if departure_bool:
        print("\nChoose your departure place")
    
        if data[0] == 0 or data[0] == 1:
            for i in city:
                print(str(departure_index) + ". " + i)
                departure_index += 1

            while inputDeparture_bool:
                inputDeparture = int(input("Input number only: "))
                if inputDeparture >= 0 and inputDeparture <= 30:
                    inputDeparture_bool = False
                    print("You choose", city[inputDeparture])
                
                    if inputDeparture == 30:
                        quitBool = True
                else:
                    print("Invalid input")
        elif data[0] == 2:
            for i in harbour:
                print(str(departure_index) + ". " + i)
                departure_index += 1

            while inputDeparture_bool:
                inputDeparture = int(input("Input number only: "))
                if inputDeparture >= 0 and inputDeparture <= 28:
                    inputDeparture_bool = False
                    print("You choose", harbour[inputDeparture])
                
                    if inputDeparture == 28:
                        quitBool = True
                else:
                    print("Invalid input")

        if quitBool:
            return print("\nGood bye!")
        else:
            destination_bool = True
        
        data.append(inputDeparture)
        
    return destination_bool

def destination(destination_bool,data):
    inputDestination_bool = True
    time_bool = False
    quitBool = False
    destination_index = 0

    if destination_bool:
        print("\nChoose your destination place")
    
        if data[0] == 0 or data[0] == 1:
            for i in city:
                print(str(destination_index) + ". " + i)
                destination_index += 1

            while inputDestination_bool:
                inputDestination = int(input("Input number only: "))
                if inputDestination == data[2]:
                    print("Seriously?")
                
                elif inputDestination >= 0 and inputDestination <= 30:
                    inputDestination_bool = False
                    print("You choose", city[inputDestination])
                    
                    if inputDestination == 30:
                        quitBool = True
                        
                else:
                    print("Invalid input")
            data.append(city[inputDestination])
        elif data[0] == 2:
            for i in harbour:
                print(str(destination_index) + ". " + i)
                destination_index += 1

            while inputDestination_bool:
                inputDestination = int(input("Input number only: "))
                if inputDestination == data[2]:
                    print("Seriously?")
                    
                elif inputDestination >= 0 and inputDestination <= 28:
                    inputDestination_bool = False
                    print("You choose", harbour[inputDestination])
                
                    if inputDestination == 28:
                        quitBool = True
                
                else:
                    print("Invalid input")
            data.append(harbour[inputDestination])
        if quitBool:
            return print("\nGood bye!")
        else:
            time_bool = True            
    
    return time_bool

def time(time_bool):
    inputTime_bool = True
    seat_bool = False
    if time_bool:
        print("\nChoose your departure time")
        print("Departure time only available for 06:00, 12:00, and 18:00 Western Indonesia Time")
        
        while inputTime_bool:
            inputDate = int(input("Input Departure Date (1-31): "))
            inputMonth = int(input("Input Departure Month (1-12): "))
            inputYear = int(input("Input Departure Year (2021 or 2022): "))
            inputTime = int(input("Input Departure Time (6/12/18): "))
            
            # Using Date Validation Program
            inputTime1_bool = val.valid1(inputDate,inputMonth,inputYear)
            inputTime2_bool = val.valid2(inputTime)
            
            if inputTime1_bool and inputTime2_bool:
                seat_bool = True
                break
            else:
                print("Invalid time input! Please input valid time\n")
            
            
        print("You choose ", inputDate,"/", inputMonth, "/", inputYear, " at ", inputTime, ":00 Western Indonesia Time",sep="")
        data.append(inputDate)
        data.append(inputMonth)
        data.append(inputYear)
        data.append(inputTime)
            
    return seat_bool

def seat(seat_bool):
    inputSeat_bool = True
    train_bool = False
    plane_bool = False
    ship_bool = False
    quitBool = False
    
    if seat_bool:
        print("\nChoose your seat")
    
        if data[0] == 0:
            train.train()
            train_bool = True
        
        elif data[0] == 1:
            if data[1] == 0:
                plane.economy_class()
            elif data[1] == 1:
                plane.business_class()
            elif data[1] == 2:
                plane.vip_class()
            plane_bool = True
        
        elif data[0] == 2:
            if data[1] == 0:
                ship.economy()
            elif data[1] == 1:
                ship.business()
            elif data[1] == 2:
                ship.vip()
            ship_bool = True
    
        while inputSeat_bool:
            inputSeat = input("\nInput your seat id (input 'cancel' to cancel ordering ticket): ")
        
            if inputSeat == "cancel":
                quitBool = True
                inputSeat_bool = False
                
            elif train_bool:
                if train.checkTrain_ID(inputSeat):
                    inputSeat_bool = False
                
            elif plane_bool:
                if plane.checkPlane_ID(inputSeat):
                    inputSeat_bool = False
            
            elif ship_bool:
                if ship.checkShip_ID(inputSeat):
                    inputSeat_bool = False
        
    
        if quitBool:
            return print("\nGood Bye!")
        else:
            data.append(inputSeat)
            price_bool = True
        
        return price_bool

def price(price_bool):    
    Domestic = False
    International= False    
    price_city = [["Medan","Jakarta","Batam","Surabaya","Bandung","Yogyakarta"],["London","Moskow","Paris","Munich","Berlin","Madrid","New York","Washington DC","Manchester","Dubai","New Delhi","Beijing","Singapore","Hongkong","Rome","Rio de Janeiro","Cape Town","Manila","Kuala Lumpur","Bangkok","Hongkong","Seoul","Tokyo","Monterrey","Cancel Ordering Ticket"]]
    price_harbour = [["Medan","Batam"],["Hongkong","Guangzhou","Busan","Cape Town","Piraeus","Rotterdam","Kopenhagen","Shanghai","Jeddah","Bursaid","Port Royal","Ho Chi Minh","Santos","Valencia","Vanesia","Rio de Janeiro","Sydney","Amsterdam","Lindau","Hamburg","New York","Mumbai","Manila","Tanjung Perak","Nagoya","Khor Fakkan","Cancel Ordering Ticket"]]

    if price_bool:        
        if data[0] == 1 or data[0] == 0:
            for i in range(len(price_city)):            
                for j in range(len(price_city[i])):                    
                    if data[3] == price_city[i][j]:                        
                        if(i == 0):
                            Domestic = True                       
                        else:
                            International = True
                            
        elif data[0] == 2:                    
            for i in range(len(price_harbour)):
                for j in range(len(price_harbour[i])):
                    if data[3] == price_harbour[i][j]:
                        if(i == 0):
                            Domestic = True                    
                        else:
                            International = True
                            
        if data[0] == 0:
            price = 100000
        elif data[0] == 1:
            price = 500000
        elif data[0] == 2:
            price = 250000

        if data[1] == 0:
            grade_price = 0
        elif data[1] == 1:
            grade_price = 10/100 * price
        elif data[1] == 2:
            grade_price = 50/100 * price

        if(Domestic):
            transport_price = 200000
        elif(International):
            transport_price = 500000
                            
        total_price = price + grade_price + transport_price
        data.append(total_price)
        return total_price
    
def correct():
    inputCorrect_bool = True
    
    while inputCorrect_bool:
        print('\nPlease check the receipt and confirm')
        inputCorrect = input('("Y" = Confirm; "N" = Cancel Ordering Ticket)')

        if inputCorrect == "Y":
            inputCorrect_bool = False
            return closing()
        
        elif inputCorrect == "N":
            inputCorrect_bool = False
            return print("Good Bye !")
        
def closing():
    print("Have a nice day ^^")
'''
data[0] = Ticket Type
data[1] = Ticket Class
data[2] = Departure
data[3] = Destination
data[4] = Date
data[5] = Month
data[6] = Year
data[7] = Time
data[8] = Seat ID
data[9] = Total Price
'''