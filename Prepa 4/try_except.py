#Sirve mas que todo para validar
#try lo intenta y si se produce un error va para el except

while True:
    try:
        numero=int(input("coloque un numero"))
        break
    except:
        print("ERROR")

#Validacion de strings
while True:
    try:
        palabra=input("coloque una palabra ")
        if palabra.isalpha()==False:
            raise ValueError
        else:
            break 
    except:
        print("caracter invalido ")