from drink import Drink

class Alcohol(Drink):
    def __init__(self,name,brand,alcohol,tipe):
        super().__init__(name,brand,alcohol,tipe)
        self.can_alcohol=alcohol
        self.tipe=tipe