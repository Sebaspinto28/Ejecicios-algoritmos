from Evento import Evento
from Artista import Artista,Musico,DJ,Comediante

class App:
    def __init__(self):
        self.eventos=[]
        self.artistas=[]
        self.musicos=[]


           
    def registros(self,datos):
        for objeto,lista in datos.items():
            for dato in lista:
                if objeto=="eventos":
                    evento=Evento(id=dato["id"],tipo=dato["tipo"],fecha=dato["fecha"],duracion=dato["duracion"],lugar=dato["lugar"])
                    self.eventos.append(evento)
                elif objeto == "artistas":
                    for dato in lista:
                        artista=Artista(nombre=dato["nombre"],biografia=dato["biografia"],tipo=dato["tipo"],tarifa_hora=["tarifa_hora"],evento=["eventos"])
                        self.artistas.append(artista)
                
    def agregar_evento(self):
        tipo=input("que tipo de evento es")
        fecha=input("cuando va ser ")
        hora=input("a que hora es ")
        duracion=input("cuanto va a durar")
        lugar=input("en donde se realizara")
        artistas=input("artista involucrado")
        evento=Evento(tipo,fecha,hora,duracion,lugar,artistas)
        self.eventos.append(evento)

    def show_eventos(self):
        for evento in self.eventos:
            print(evento.show_attr())
    def agregar_artista(self):
        nombre=input("nombre del artista")
        biografia=input("biografia del artista")
        tipo=input("que tipo de artista es 1.musico\n 2.dj \n 3.comediante\n-->")
        if tipo=="1":
            instrumento=input("que instrumento toca")
            artista=Musico(nombre,tipo,instrumento)
        elif tipo=="2":
            genero=input("que genero de musica toca")
            artista=DJ(nombre,tipo,genero)
        elif tipo=="3":
            estilo=input("que estilo de comedia hace")
            artista=Comediante(nombre,tipo,estilo)
        self.artistas.append(artista)  
    

    def tasa_artista(self):
        for artista in self.artistas:
            for evento in self.eventos:
                print(f"el artista {artista.nombre}\n cuesta {artista.tarifa_h*evento.tiempo}\n Evento{artista.evento}")

    def start(self,datos):
        self.registros(datos)
        
        print("Bienvenido")
        while True:
            try:
                menu=input("\n Ingrese una de las opciones\n 1. Ver eventos\n 2. Agregar eventos\n 3. Comfirmar entrega\n 4. Agregar artista \n 5. Tarifa del artista\n6. \n7.salir\n --->")
                if menu == "1":
                    self.show_eventos()
                elif menu == "2":
                    self.agregar_evento()    
                elif menu=="3":
                    pass
                elif menu=="4":
                    self.agregar_artista()
                elif menu=="5":
                    self.tasa_artista()
                elif menu=="6":
                    pass
                elif menu=="7":
                    print("Hasta luego")
                    break
                else:
                    raise ValueError
            except:
                print('Dato invalido')
