oracion=(input("ingrse la oracion\n--->"))
#la caracola esta enterrada al lado de otra caracola de color 
oracion_separada=oracion.split(" ")

words=[]
repetidas=[]
for palabra in oracion_separada:
    if words.count(palabra)==0:
        words.append(palabra)

for palabra in words:
     repeticion=oracion.count(palabra)
     print(palabra,"-->",repeticion)

if repeticion>1:
    repetidas.append(palabra)
print(repetidas)