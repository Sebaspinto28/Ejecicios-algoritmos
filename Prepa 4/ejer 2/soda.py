from drink import Drink

class Soda(Drink):
    def __init__(self,name,brand,sugar):
        super().__init__(name,brand)
        self.can_sugar=sugar