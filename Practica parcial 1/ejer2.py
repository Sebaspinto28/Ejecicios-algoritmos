
def show_welcome():
    print("Bienvenido a la serie del Saman")
def cant_entradas(option,numero):
    if option=="1":
        precio=45*numero 
    else:
        precio=65*numero  
    return precio
def descuento(numero,sub_total):
    numero=numero%2
    if numero!=0:
        des=sub_total-(sub_total*0.10)
        
        return des
    else:
        return sub_total
def desicion():
    que=str(input("Desea continua\nEscoja si o no "))
    if que =="si":
        return True
    else:
        print("Hasta luego")
        return False
def opcion_1(cant_descuentos,cant_general,cant_vip):
   
    nombre=str(input(" Escriba su nombre y apellido\n-->")).lower()
    cedula=int(input("introdusca su cedula-->"))
    correo=(input("introdusca su correo electronico-->"))
    option=(input("que entrda decesa comprar\n1.GENERAL\n2.VIP\n-->"))
    numero=int(input("Cuantas entradas desea-->"))
    sub_total=cant_entradas(option,numero)
    total=descuento(numero,sub_total)
    if option=="1":
        cant_general+=numero
        print(f"el precio a pagar es {total}")
    elif option=="2":
        cant_vip+=numero
        hambu=numero*2
        print(f"el precio a pagar es {total} y tienes {hambu} hamburguesas")
    if desicion()==True:
        print("nombre: ",nombre,"\ncedula: ",cedula,"\ncorreo: ",correo)
        print(numero, "entradas: ", "General"if option==1 else "VIP")
    else:
        print("chao")
        
    if numero%2!=0:
        cant_descuentos+=numero
    return cant_descuentos,cant_general,cant_vip
def main():
    cant_descuentos=0
    cant_general=0
    cant_vip=0
    show_welcome()
    while True:
        opti=(input("que desea hacer\n1.compras \n2.estadisticas\n3.salir\n-->"))
        if opti=="1":
            cant_descuentos,cant_general,cant_vip=opcion_1(cant_descuentos,cant_general,cant_vip)
        elif opti=="2":
            
            print(f"cantidad de desceuntos otorgados {cant_descuentos}")
            print(f"cantidad de entradas generales vendidas {cant_general}")
            print(f"cantidad de entradas vip vendidas {cant_vip}")
        else:
            print("Hasta luego")
            break
main()
    

