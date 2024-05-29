def welcome():
    print("Bienvenido a autoescuela La rapida")

def val_cedula(cedula):
    while not  cedula.isnumeric() or not len(cedula) in range(7,9):
        print("ERROR")
        cedula=input("Ingrese su cedula")
    return cedula

def val_caja(caja):
    while not caja.isnumeric() or not int(caja) in range(1,3):
        print("ERROR")
        caja=input('''Diga que tipo de de vehiculo esta manejando\n1)Automatico\n2)sincronico\n-->''')
    return caja 
    

    
def val_hora(hora):
    while not hora.isnumeric() or not int(hora) in range(1,9):
        print("Epa por aqui no es ")
        hora=input("coloque el numero de horas que vera en su clase\nm-->")
    return hora

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
   

def opcion_1(con_cli,con_a,con_s,con_des,con_pro_a,con_pro_s):

    cedula=input("Ingrese su cedula")
    con_cli+=1
    cedula=val_cedula(cedula)

    caja=input("Diga que tipo de de vehiculo esta manejando\n1)Automatico\n2)sincronico\n--> ")
    caja=val_caja(caja)

    hora=input("coloque el numero de horas que vera en su clase\nm-->")
    hora=val_hora(hora)

    if caja=="1":
        precio=2500
        con_a+=1
        con_pro_a+=precio
    elif caja=="2":
        con_s+=1
        precio=3500
        con_pro_s+=precio
        
    if int(hora)>3:
        con_des+=1
        
        precio=precio*0.75
    lista=[]
    for i in cedula:
        lista.append(i)
    
    n=lista[-1]
    x=int(n)
    
    if is_prime(x):
        con_des+=1
        precio=precio*0.80
    print("Cedula--->",cedula)
    print("Tipo de vehiculo---> ","Automatico" if caja=="1" else "Sincronico")
    print("Precio a cancelar--->",precio)
    return con_cli,con_a,con_s,con_des,con_pro_a,con_pro_s

def main():
    welcome()
    con_cli=0
    con_a=0
    con_s=0
    con_des=0
    con_pro_a=0
    con_pro_s=0
    while True:
        opcion=(input("Que desea realizar\n1. Facturar\n2. Ver estadisticas\n3. Salir\n--->"))
        if opcion =="1":
            con_cli,con_a,con_s,con_des,con_pro_a,con_pro_s=opcion_1(con_cli,con_a,con_s,con_des,con_pro_a,con_pro_s)
        elif opcion=="2":
            print(f"Clientes: {con_cli}\nAutomatico: {con_a}\nsincronico: {con_s}\nDescuentos: {con_des}\nPromedio de automaticos: {con_pro_a/con_a}\nPromedio de sincronicos: {con_pro_s/con_s}")
        else:
            break
main()