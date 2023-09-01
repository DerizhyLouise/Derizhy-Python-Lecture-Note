def valid1(date,month,year):
    y = True
    n = False

    yearValidity = False
    leap = False
    monthValidity = False

    if(year >= 2021 and year <= 2022):
        yearValidity = True

    if(year%4 == 0):
        leap = True
    
    if(month > 0 and month <= 12):
        monthValidity = True

    if(month == 1):
        maxDate = 31
    elif(month == 2):
        if(leap):
            maxDate = 29
        else:
            maxDate = 28
    elif(month == 3):
        maxDate = 31
    elif(month == 4):
        maxDate = 30
    elif(month == 5):
        maxDate = 31
    elif(month == 6):
        maxDate = 30
    elif(month == 7):
        maxDate = 31
    elif(month == 8):
        maxDate = 31
    elif(month == 9):
        maxDate = 30
    elif(month == 10):
        maxDate = 31
    elif(month == 11):
        maxDate = 30
    elif(month == 12):
        maxDate = 31

    if(yearValidity and leap and monthValidity):
        if(date <= maxDate):
            return y
        else:
            return n
    elif(yearValidity and monthValidity):
        if(date <= maxDate):
            return y
        else:
            return n
    else:
        return n
    
def valid2(time):
    y = True    
    n = False
    if time == 6 or time == 12 or time == 18:
        return y
    else:
        return n