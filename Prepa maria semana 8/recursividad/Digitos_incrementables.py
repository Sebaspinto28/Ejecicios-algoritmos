def incremental(numero):
    if len(numero) ==1:
        return True
    else:
        if numero[0]<=numero[1]:
            return incremental(numero[1:])
        else:
            return False

def main():
    while True:
        try:
            numero=int(input("ingrese un numero entero\n--->"))
            if numero<0:
                raise ValueError
            #incremental num debe ser string
            valor= incremental(str(numero))
            if valor==True:
                print("El numero es incremental")
            else:
                print("El numero no es incremental")
            continue
        except:
            print("Error, ingrese un numero entero positivo")

main()
        