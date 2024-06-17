from Cliente import Cliente
from Paquete import Paquete
from Envio import Maritimo
from Envio import Aereo

def menu():
    menu=input('''
        ***Menu***
               
    1- crear paquete
    2- ver estatus
    3- actualizar estado
    4- estadisticas
    5- salir
''')
    return menu

def crear_paquete(num_paquete,ciudades):
    nombre=input("Coloque su nombre")
    dni=input("Coloque su dni")
    telefono=input("Coloque su telefono")

    ##envio##
    origen=input("De donde envia")
    cont=0
    for destino in ciudades:
        cont+=1
        print(f" {cont}- {destino[0]}")

    print(f" {cont+1}- Otro")
    destino=int(input(" Ingresa: "))

    if destino-1 == len(ciudades):
        destino=input("Ingresa la nueva ciudad: ")
        cant=1
        aux=[destino,cant]
        ciudades.append(aux)
    
    else:
        ciudades[destino-1][1]+=1


    tipo_e=input("Que tipo de envio: \n1.Maritimo \n2.Aereo\n--->")
    cliente=Cliente(nombre,dni,telefono)
    num_paquete=num_paquete
    fecha=input("Fecha  de llegada")
    status=input("ingrese el estatus")
    ##PAQUETE##
    peso=int(input("Ingrese peso en kilos"))
    largo=int(input("Ingrese peso en largo en m"))
    alto=int(input("Ingrese peso en alto en m"))
    ancho=int(input("Ingrese peso en amcho en m"))
    valor=int(input("Ingrese el valor declarado"))
    while True:
        tipo=(input("Que tipo de cosas tiene el paquete:\n1.documento \n2.comida \n3.ropa \4.electrodomesticos \5.otros\n--->"))
        if tipo_e=="2" and tipo=="2":
            print("ERROR no se puede llevar comida en aereo")
        else:
            break
    


    paquete=Paquete(peso,largo,ancho,alto,valor,tipo)
    if tipo_e=="1":
        envio=Maritimo(origen,destino,cliente,num_paquete,fecha,status,paquete)  
    else:
        envio=Aereo(origen,destino,cliente,num_paquete,fecha,status,paquete)
    
    

    costo = int(envio.costo())

    for x in range(1,costo):
        factorial=1
        n=x
        count=1

        while count <=n:
            factorial*=count
            count+=1

        if factorial>=costo:
            if factorial==costo:
                descuento=costo*0.10
            else:
                descuento=0
            break

    print(f"El precio del envio es{costo-descuento} y su numero de seguimiento es: {envio.tracking}")
    return envio, ciudades

def ver_status(envios):
    num_seg=int(input())
    for x in envios:
        print(x)
        if x.tracking == num_seg:
            print(x.status)

def actualizar_status(envios):
    num_seg=int(input())
    for x in envios:
        if x.tracking == num_seg:
            x.status=input("ingrese nuevo estatus")

def main():
    num_paquete=0
    envios=[]
    ciudades=[]
    
    while True:
        
        option=menu()
        if option=="1":
            num_paquete+=1
            emp, ciudades =crear_paquete(num_paquete, ciudades)
            envios.append(emp)

        elif option=="2":
            ver_status(envios)

        elif option=="3":
            actualizar_status(envios)

        elif option=="4":
            ciudades = sorted(ciudades, key=lambda ciudad: ciudad[1])
            print(f"LA ciudad mas comun es {ciudades[-1][0]}")
            print()
        elif option=="5":
            break
        else:
            print("Ingrese un numero valido")


main()