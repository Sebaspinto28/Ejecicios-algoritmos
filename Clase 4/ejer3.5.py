def val_numero(numero):
    while not numero.isnumeric or not int(numero):
        print("ERROR")
        numero=input("ingrsese el numero \n--> ")
    return numero 

def main():
    lista1=[]
    numero=input("ingrese el numero\n--> ")
    numero=val_numero(numero)
    
    for i in numero:
        lista1.append(i)
    if lista1==lista1[::-1]:
        print("es palindromo ")
    else:
        print("no es palindromo ")
main()