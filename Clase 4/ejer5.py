'''Escribe un programa en Python que simule un juego de adivinanzas.
El programa debe iterar una lista de palabras para adivinar.
El jugador debe intentar adivinar la palabra en un número limitado de intentos (5 intentos).
El programa debe llevar un registro de los intentos realizados y mostrar un mensaje al jugador
indicando si adivinó la palabra o no.  Cada vez que el jugador hace un intento, se le muestra cuántas
letras ha adivinado correctamente. El juego utiliza listas para almacenar los intentos realizados
y al final muestra en un diccionario las palabras que fueron adivinadas para cada una de ellas.

palabras = ["chocolate", "agua", "espejo"]
resultado = {‘chocolate’: [‘choco’, ‘afro’, ‘chocolate’], ‘agua’: [‘techo’, ‘comida’, ‘agua’], ‘espejo’: [‘espejo’]}'''


#print("bienvenido a su juego de palabras XD")
#pala=str(input("Escriba la palabra qu usted crea que es la correcta\n-->"))
#words=["chocolate", "agua", "espejo"]
#dic={"chocolate":["c","h","o","c","o","l","a","t","e",]}
#chocolate=[]
#cosa=True
#for i in range(0):
#    if pala!=words[0]: 
#        chocolate.append(pala)
#        palabra_separada=list(pala)
#        for j in range(len(palabra_separada)):
#
#
#
#
#
#
#
#    else:
#        cosa=True
#        
#
#    pala=str(input("Escriba la palabra qu usted crea que es la correcta\n-->"))
#
#if cosa==True:
#    print("ok")
#        
#print(list(pala))

palabras = ["chocolate", "agua", "espejo"]
resultado = {}
letras_adivinadas = []

print("JUEGO DE ADIVINANZAS\n")
for palabra in palabras:
    intentos = 5
    answer = ""

    resultado[palabra] = []
    while True:
        print(f"La palabra tiene {len(palabra)} letras")
        answer = input("\tIntroduzca su intento: ")

        if answer == palabra:
            print("FELICIDADES. Ha acertado.")
            resultado[palabra].append(answer)
            print("SIGUIENTE PALABRA\n")
            break
        else:
            print("INCORRECTO")
            resultado[palabra].append(answer)

            letras_adivinadas = []
            for letra in answer:
                if letra in palabra and letra not in letras_adivinadas:
                    letras_adivinadas.append(letra)
            print(f"HA ADIVINADO LAS SIGUIENTES LETRAS: {letras_adivinadas}")
            intentos -= 1
            
            if intentos == 0:
                print("SE HA QUEDADO SIN INTENTOS\n\nSIGUIENTE PALABRA")
                break

print(f"RESULTADO FINAL:\n{resultado}")