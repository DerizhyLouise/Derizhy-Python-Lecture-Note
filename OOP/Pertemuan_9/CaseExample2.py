class inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)
        
    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self.product = value
        self.update_observers()
        
    @property
    def quantity(self):
        return self._product
    
    @quantity.setter
    def quantity(self, value):
        self.quantity = value
        self.update_observers()
        
    def _update_observers(self):
        for observer in self.observers:
            observer()
            
class consoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

i = inventory
c1 = consoleObserver(i)
c2 = consoleObserver(i)
i.attach(c1)
i.attach(c2)
i.product = "Gadget"