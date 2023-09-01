from abc import ABC, abstractmethod

class Browser(ABC):
    @abstractmethod
    def createSearchToolbar(self):
        pass
    @abstractmethod
    def createBrowserWindow(self):
        pass
    
class Messenger(ABC):
    @abstractmethod
    def createMessengerWindow(self):
        pass
    
class VanillaBrowser(Browser):
    def createSearchToolbar(self):
        print("Search Toolbar Created")
    def createBrowserWindow(self):
        print("Browser Window Created")

class VanillaMessenger(Messenger):
    def createMessengerWindow(self):
        print("Messenger Window Created")

class SecureBrowser(Browser):
    def createSearchToolbar(self):
        print("Secure Browser - Search Toolbar Created")
    def createBrowserWindow(self):
        print("Secure Browser - Browser Window Created")
    def createIncognitoMode(self):
        print("Secure Browser - Incognito Mode Created")
        
class SecureMessenger(Messenger):
    def createMessengerWindow(self):
        print("Secure Messenger - Messenger Window Created")
    def createPrivacyFilter(self):
        print("Secure Messenger - Privacy Filter Created")
    def disappearingMessages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")
        
class AbstractFactory(ABC):
    @abstractmethod
    def createBrowser(self):
        pass
    @abstractmethod
    def createMessenger(self):
        pass
    
class VanillaProductFactory(AbstractFactory):
    def createBrowser(self):
        return VanillaBrowser()
    def createMessenger(self):
        return VanillaMessenger()
    
class SecureProductFactory(AbstractFactory):
    def createBrowser(self):
        return SecureBrowser()
    def createMessenger(self):
        return SecureMessenger()
    
if __name__ == '__main__':
    for factory in (VanillaProductFactory(), SecureProductFactory()):
        productA = factory.createBrowser()
        productB = factory.createMessenger()
        productA.createBrowserWindow()
        productA.createSearchToolbar()
        productB.createMessengerWindow()