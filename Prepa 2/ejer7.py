nombre=(input("escriba su nombre"))
apellido=(input("escriba su apellido"))
code = {
"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":1,"k":2,"l":3,"m":4,"n":5,"ñ":5,"o":6,"p":7,"q":8,"r":9,"s":1
,"t":2,"u":3,"v":4,"w":5,"x":6,"y":7,"z":8
}

vocales_nombre=[]
vocales_apellido=[]
consonates_nombre=[]
consonate_apellido=[]
for letra in nombre.lower():
    if letra in "aeiou":
        vocales_nombre.append(letra)

for letra in apellido.lower():
    if letra in "aeiou":
        vocales_apellido.append(letra)

for letra in nombre.lower():
    if letra in code and letra not in "aeiou":
        consonates_nombre.append(letra)

for letra in apellido.lower():
    if letra in code and letra not in "aeiou":
        consonate_apellido.append(letra)

suma_vocales=sum(code[letra])
for letra in vocales_nombre:

    print(vocales_nombre, vocales_apellido, consonates_nombre, consonate_apellido)