class subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} got message '{message}'")
        
class publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

pub = publisher()

bob = subscriber("Bob")
alice = subscriber("Alice")
john = subscriber("John")

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunch time!")