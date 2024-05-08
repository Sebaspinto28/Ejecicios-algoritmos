correo=(input("Escriba su direccion de correo electronico: EJ:juanita@gmail.com\n"))
if (correo.count("@")==1):  
    if correo.count(".")>=1:
        print(f"su direccion de correo electronico: {correo} es valido.")
    else:
        print("correo invalido")
else:
    print("correo invalido =")