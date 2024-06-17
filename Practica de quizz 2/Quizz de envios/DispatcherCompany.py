class DispatcherCompany:
    def __init__(self,id,name,products):
        self.id = id
        self.name = name
        self.packages =products

    def show_attr(self):
        return f"ID:{self.id}\nNombre:{self.name}\nPaquetes:{self.show_packages()}"

    def show_packages(self):
        cadena=""
        for i,paquete in enumerate(self.packages):
            cadena += f" \n   {i+1}. {paquete.show_attr()}"
        return cadena 


