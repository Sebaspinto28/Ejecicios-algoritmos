from Producto import Postre,Cafe,Jugo
from Cliente import Cliente
class App:
    def __init__(self) -> None:
        self.postres=[]
        self.cafes=[]
        self.jugos=[]
        self.clientes=[]

    def registro(self,menu):
        for objeto,lista in menu.items():
            for datos in lista:
                if objeto=="postres":
                    postre=Postre(id=len(self.postres) +1,nombre=datos["nombre"],precio=datos["precio"],cantidad=datos["cantidad"],es_vegano=datos.get("es_vegano",False))
                    self.postres.append(postre)
                
                elif objeto=="cafes":
                    cafe=Cafe(id=len(self.cafes)+1,nombre=datos["nombre"],precio=datos["precio"],cantidad=datos["cantidad"],tamano=datos["tamaño"],es_descaifenado=datos["es_descafeinado"])
                    self.cafes.append(cafe)
                
                elif objeto=="jugos":
                    jugo=Jugo(id=len(self.jugos),nombre=datos["nombre"],precio=datos["precio"],cantidad=datos["cantidad"],sabor=datos["sabor"],contiene_azucar=datos["contiene_azucar"])
                    self.jugos.append(jugo)

    def registro_cliente(self):
        nombre=str(input("escriba su nombre"))
        edad=int(input("escriba su edad"))
        cedula=int(input("escriba su cedula"))

        cliente=Cliente(nombre,edad,cedula)
        self.clientes.append(cliente)
        print(f"Se ha resgistardo con exito:{cliente.show_attr()}")

    def show_menu(self):
        print("Menu")
        print("Postres")
        for postre in self.postres:
            print(postre.show_attr())
        print("Cafes")
        for cafe in self.cafes:
            print(cafe.show_attr())
        print("Jugos")
        for jugo in self.jugos:
            print(jugo.show_attr())

    def show_clientes(self):
        print("Clientes")
        for cliente in self.clientes:
            print(cliente.show_attr())

    def comprar(self):
        print("Seleccione el producto que desea comprar")
        print(self.show_menu())
        registra=self.registro_cliente()
        

        que=input("Que dece comprar:\n1.Postres\n2.Cafe\n3.Jugos\n--->")
        if que=="1":
            id=int(input("escriba el id del postre que dece comprar\n--->"))
            for postre in self.postres:
                if postre.id==id:
                    print(f"Ha comprado un {postre.nombre} por {postre.precio}")
                    
        elif que=="2":
            id=int(input("escriba el id del cafe que dece comprar\n--->"))
            for cafe in self.cafes:
                if cafe.id==id:
                    print(f"Ha comprado un {cafe.nombre} por {cafe.precio}")
                    
                    
        elif que=="3":
            id=int(input("escriba el id del jugo que dece comprar\n--->"))
            for jugo in self.jugos:
                if jugo.id==id:
                    print(f"Ha comprado un {jugo.nombre} por {jugo.precio}")
                    

            

    def start(self,menu):
        print("BIENVENIDO A LA CAFETERIA")
        self.registro(menu)
        print("Bienvenido al despacho")
        while True:
            try:
                menu=input("\n Ingrese una de las opciones\n 1. Ver el menu \n 2. Crear cliente \n 3. ver clientes \n 4.Comprar \n 5.Salir \n --->")
                if menu == "1":
                    self.show_menu()
                elif menu == "2":
                    self.registro_cliente()    
                elif menu=="3":
                    self.show_clientes()
                elif menu=="4":
                    self.comprar()
                elif menu=="5":
                    print("Hasta luego")
                    break
                else:
                    raise ValueError
            except:
                print('Dato invalido')
