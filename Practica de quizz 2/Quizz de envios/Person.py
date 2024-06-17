class Person:
    def __init__(self,id, name):
        self.id = id
        self.name = name
    
    def show_attr(self):
        return f"\nID:{self.id}\nNombre:{self.name}"

class Worker(Person):
    def __init__(self, id, name,role,dispatches):
        super().__init__(id, name)
        self.role=role
        self.dispatches=dispatches

    def show_attr(self):
        return f"{super().show_attr()}\nRole:{self.role}\nDespachos:{self.dispatches}"
    
class Client(Person):
    def __init__(self, id, name, address):
        super().__init__(id, name)
        self.address = address
    def show_attr(self):
        return f"{super().show_attr()}\nRole:{self.address}"
    