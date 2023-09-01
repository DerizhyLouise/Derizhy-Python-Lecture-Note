import abc

class syaratTask1 (metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def nomorInduk (self):
        pass
    
    @abc.abstractproperty
    def nama (self):
        pass
    
    @abc.abstractproperty
    def gender (self):
        pass
    
    @abc.abstractproperty
    def noHP (self):
        pass
    
    @abc.abstractmethod
    def cetakData (self):
        pass
    
class syaratTask2 (metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def nama (self):
        pass
    
    @abc.abstractproperty
    def noHP (self):
        pass
    
    @abc.abstractmethod
    def biayaLes (self):
        pass