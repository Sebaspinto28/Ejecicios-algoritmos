class Packages:
    def __init__(self,id,address,delivered):
        self.id = id
        self.address = address
        self.delivered = delivered

    def show_attr(self):
        return f"ID:{self.id}\nDireccion:{self.address}\n Deliverado: {self.ask_delivered()}"

    def ask_delivered(self):
        if (self.delivered): # Yo pienso que es asi , ella hace if (self.delivered):
            return "Si"
        else:
            return "No"
        
    