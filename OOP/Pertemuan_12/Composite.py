from abc import ABC, abstractmethod

class item(ABC):
    @abstractmethod
    def returnPrice(self):
        pass
    
class box(item):
    def __init__(self, contents):
        self.contents = contents
    def returnPrice(self):
        price = 0
        for item in self.contents:
            price = price + item.returnPrice()
        return price
    
class phone(item):
    def __init__(self, price):
        self.price = price
    def returnPrice(self):
        return self.price
    
class charger(item):
    def __init__(self, price):
        self.price = price
    def returnPrice(self):
        return self.price
    
class earphones(item):
    def __init__(self, price):
        self.price = price
    def returnPrice(self):
        return self.price
    
if __name__ == '__main__':
    phoneCaseContents = []
    phoneCaseContents.append(phone(200))
    phoneCaseBox = box(phoneCaseContents)
    bigBoxContents = []
    bigBoxContents.append(phoneCaseBox)
    bigBoxContents.append(charger(10))
    bigBoxContents.append(earphones(100))
    bigBox = box(bigBoxContents)
    
    print("Total price : ", bigBox.returnPrice())