from caballo import Caballo
from carrera import Carrera 
from valida import Valida
def  crear_caballos(caballos):
    caballos.append(Caballo("rayo veloz",1))
    caballos.append(Caballo("negro",2))
    caballos.append(Caballo("McQueen",3))
    caballos.append(Caballo("Spidy",4))
    caballos.append(Caballo("Franchesco",5))
    caballos.append(Caballo("Alga",6))

def crear_carreras(carreras,caballos,cantidad_carreras):
    for i in range(cantidad_carreras):
        

    
def crear_validas(validas):
    pass
def main():
    caballos=[]
    carreras=[]
    validas=[]
    cantidad_carreras=int(input("cuantas carreras quieres por valida"))
    crear_caballos(caballos)
    crear_carreras(carreras)
    crear_validas(validas)


main()